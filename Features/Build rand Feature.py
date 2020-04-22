#MenuTitle: Build rand Feature
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
__doc__="""
Build rand (random) feature from .cvXX or another (numbered) suffix.
"""

import vanilla

def getRootName(glyphName):
	if "." in glyphName:
		dotIndex = glyphName.find(".")
		return glyphName[:dotIndex]
	else:
		return glyphName

class BuildRandFeature( object ):
	def __init__( self ):
		# Window 'self.w':
		windowWidth  = 320
		windowHeight = 130
		windowWidthResize  = 100 # user can resize width by this value
		windowHeightResize = 0   # user can resize height by this value
		self.w = vanilla.FloatingWindow(
			( windowWidth, windowHeight ), # default window size
			"Build rand Feature", # window title
			minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
			maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
			autosaveName = "com.mekkablue.BuildRandFeature.mainwindow" # stores last window position and size
		)
		
		# UI elements:
		linePos, inset, lineHeight = 12, 15, 22
		
		self.w.descriptionText = vanilla.TextBox( (inset, linePos+2, -inset, 14), u"Build a Randomize feature with the following suffix:", sizeStyle='small', selectable=True )
		linePos += lineHeight
		
		self.w.suffixText = vanilla.TextBox( (inset, linePos+3, 45, 14), u"Suffix:", sizeStyle='small', selectable=True )
		self.w.suffix = vanilla.ComboBox( (inset+45, linePos, -inset-25, 17), self.fillSuffixes(), sizeStyle='small', callback=self.SavePreferences)
		self.w.suffix.getNSComboBox().setToolTip_(u"Find all (exporting) glyphs that have this suffix and in OT feature ‘rand’, build a one-from-many substitution with them. Hint: keep the dot, but avoid the figures, e.g. for all stylistic sets, type ‘.ss’.")
		self.w.suffixReset = vanilla.SquareButton( (-inset-20, linePos, -inset, 18), u"↺", sizeStyle='small', callback=self.updateUI )
		linePos += lineHeight
		
		self.w.overwrite = vanilla.CheckBox( (inset, linePos-1, -inset, 20), u"Overwrite existing rand feature", value=True, callback=self.SavePreferences, sizeStyle='small' )
		linePos += lineHeight
		
		# Run Button:
		self.w.runButton = vanilla.Button( (-120-inset, -20-inset, -inset, -inset), "Add Feature", sizeStyle='regular', callback=self.BuildRandFeatureMain )
		self.w.setDefaultButton( self.w.runButton )
		
		# Load Settings:
		if not self.LoadPreferences():
			print("Note: 'Build rand Feature' could not load preferences. Will resort to defaults")
		
		# Open window and focus on it:
		self.w.open()
		self.w.makeKey()
		
	def SavePreferences( self, sender=None ):
		try:
			# write current settings into prefs:
			Glyphs.defaults["com.mekkablue.BuildRandFeature.overwrite"] = self.w.overwrite.get()
			Glyphs.defaults["com.mekkablue.BuildRandFeature.suffix"] = self.w.suffix.get()
			return True
		except:
			import traceback
			print(traceback.format_exc())
			return False

	def LoadPreferences( self ):
		try:
			# register defaults:
			Glyphs.registerDefault("com.mekkablue.BuildRandFeature.overwrite", 1)
			Glyphs.registerDefault("com.mekkablue.BuildRandFeature.suffix", ".cv")
			
			# load previously written prefs:
			self.w.overwrite.set( Glyphs.defaults["com.mekkablue.BuildRandFeature.overwrite"] )
			self.w.suffix.set( Glyphs.defaults["com.mekkablue.BuildRandFeature.suffix"] )
			return True
		except:
			import traceback
			print(traceback.format_exc())
			return False
	
	def updateUI(self, sender=None):
		if sender == self.w.suffixReset:
			self.w.suffix.setItems(self.fillSuffixes())
	
	def fillSuffixes(self, sender=None):
		thisFont = Glyphs.font # frontmost font
		if thisFont is not None:
			suffixes = []
			for glyph in thisFont.glyphs:
				if "." in glyph.name[1:]:
					parts = glyph.name.split(".")
					for part in parts[1:]:
						if part:
							cleanedPart = ""
							for letter in part:
								if not letter in "1234567890":
									cleanedPart += letter
							print("%s -> %s"%(part, cleanedPart))
							if cleanedPart:
								suffixes.append(".%s"%cleanedPart)
			if suffixes:
				sortedSuffixes = sorted(set(suffixes))
				return sortedSuffixes
		
		# if all else fails
		return (".cv", ".ss", ".rand", ".random")
		

	def BuildRandFeatureMain( self, sender=None ):
		try:
			# clear macro window log:
			Glyphs.clearLog()
			
			# update settings to the latest user input:
			if not self.SavePreferences():
				print("Note: 'Build rand Feature' could not write preferences.")
			
			thisFont = Glyphs.font # frontmost font
			if thisFont is None:
				Message(title="No Font Open", message="The script requires a font. Open a font and run the script again.", OKButton=None)
			else:
				print("Build rand Feature Report for %s" % thisFont.familyName)
				if thisFont.filepath:
					print(thisFont.filepath)
				else:
					print("⚠️ The font file has not been saved yet.")
				print()
				
				overwrite = Glyphs.defaults["com.mekkablue.BuildRandFeature.overwrite"]
				suffix = Glyphs.defaults["com.mekkablue.BuildRandFeature.suffix"]
				
				print("Scanning the glyph set...")
				variantDict = {}
				for thisGlyph in thisFont.glyphs:
					# populate variantDict with alternates, based on root glyph:
					if thisGlyph.export and "." in thisGlyph.name and suffix in thisGlyph.name:
						root = getRootName(thisGlyph.name)
						if not root in variantDict.keys():
							variantDict[root] = [thisGlyph.name]
						else:
							variantDict[root].append(thisGlyph.name)
				
				if not variantDict.keys():
					msg = "Could not find any dot-suffixed glyphs for building the rand feature. Aborting."
					print(msg)
					Message(title="No Glyph Variants", message=msg, OKButton=None)
				else:
					otFeatureLines = []
					for rootName in sorted(variantDict.keys()):
						altNames = sorted(variantDict[rootName])
						otFeatureLine = "sub %s from [%s];" % (
							rootName,
							" ".join(altNames),
							)
						otFeatureLines.append(otFeatureLine)
						print("🆗 %s: found %i alternate glyphs." % (rootName, len(altNames)))
						
					if not otFeatureLines:
						msg = "❌ Error. No OT feature code could be generated."
						print(msg)
						Message(title="Build rand Feature Error", message=msg, OKButton=None)
					else:
						otFeatureCode = "\n".join(otFeatureLines)
						feature = thisFont.features["rand"]
						if not feature:
							print("Building rand feature...")
							feature = GSFeature()
							feature.name = "rand"
							feature.code = otFeatureCode
							thisFont.features.append(feature)
						else:
							if overwrite:
								print("Overwriting existing rand feature...")
								feature.code = otFeatureCode
							else:
								print("Appending to existing rand feature...")
								feature.code += "\n\n# Automatic Feature Code:\n"
								feature.code += otFeatureCode
						
						print("Added %i lines of code." % len(otFeatureLines))
	
			# Final report:
			Glyphs.showNotification( 
				u"%s: Done" % (thisFont.familyName),
				u"New rand feature with %i lines available in Font Info. Details in Macro Window" % len(otFeatureLines),
				)
			print("\nDone.")

		except Exception as e:
			# brings macro window to front and reports error:
			Glyphs.showMacroWindow()
			print("Build rand Feature Error: %s" % e)
			import traceback
			print(traceback.format_exc())

BuildRandFeature()