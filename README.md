# このスクリプトについて

このスクリプトは、[Glyphs font editor](http://glyphsapp.com/)でのフォント制作を目的としたPythonスクリプトです。

# インストール

### ビデオインストールガイド

YouTubeでは、[mekkablueスクリプトのインストール方法のチュートリアルビデオ（tutorial video on how to install the mekkablue scripts）](https://www.youtube.com/watch?v=Q6ly16Q0BmE) が公開されています。視聴時にどうぞ [mekkablueチャンネル] (https://www.youtube.com/channel/UCFPSSuEMZVQtrFpTzgFh9lA) を購読してください。

### 一般的なインストール方法

スクリプトは、*Application Support*内のGlyphsの*Scripts*フォルダに置く必要があります。その方法は以下の通りです。

1. スクリプトフォルダ（またはエイリアス）を、*スクリプト > Scriptsフォルダを開く*（Cmd-Shift-Y）を選択したときに表示される*Scripts*フォルダ（`~/Library/Application Support/Glyphs/Scripts/`）に入れるか、**git**を使用します。gitについては以下を参照してください。
2. 次に、Option (Alt)キーを押しながら、*スクリプト > スクリプトメニューを更新* (Cmd-Opt-Shift-Y)を選択します。これでスクリプトが*Script*メニューに表示されます。
3. いくつかのスクリプトについては、Tal Lemingの*Vanilla:*をインストールする必要があります* *Glyphs > 環境設定 > アドオン > Pythonモジュール*に移動し、*インストールする*をクリックします。これで完了です。

### git

スクリプトを取得する際にはgitを使った方が最新の状態を維持しやすいのでおすすめです。以下のgitコマンドを使ってリポジトリを*Scripts*フォルダにクローンします。

```bash
git clone https://github.com/mekkablue/Glyphs-Scripts ~/Library/Application\ Support/Glyphs/Scripts/mekkablue/
```

ターミナルを触るのが怖いという方は、無料の [Source Tree](https://www.sourcetreeapp.com) や [GitHub Desktop](https://desktop.github.com) などのgitクライアントを使ってみましょう。

mekkablue スクリプトをインストールした後、このスクリプトリポジトリ (および *Scripts* フォルダにある他のすべてのスクリプトリポジトリ) を **update** するには、*スクリプト > mekkablue > App > Update git Repositories in Scripts Folder.* と実行します。

# トラブルシューティング

問題の報告や機能のリクエストを[GitHub issue](/issues)からお願いします。スクリプトとアプリが最新であることを確認してください。また、**必ずGlyphsとmacOSの両方のバージョンを明記してください**。


# 必要条件

スクリプトは、macOS 10.9以降で動作するGlyphs 2.xの最新バージョンが必要です。当方ではスクリプトを最新バージョンでしかテスト及び動作させることしかできません。スクリプトが動作しない場合は、まずスクリプトを最新バージョンにアップデートしてください。

# スクリプトについて

すべてのスクリプトでは、メニュー項目にマウスポインタを合わせると **ツールチップ** が表示されます。GUIを持つスクリプトでは、ほとんどのUI要素（チェックボックス、テキスト入力フィールドなど）にもツールチップが表示されます。このようにして、必要な説明を重要な場所に表示することができます。


## Anchors（アンカー）

*Anchor Mover is for batch-processing anchor positions. Can be useful after adjusting the x-height. No-brainer: I always use the Reposition script on my combining marks, so stacking combining marks stays in the italic angle.*
*アンカームーバーはアンカー位置を一括処理するためのものです。x-heightを調整した後に便利です。迷うことはありません。私はコンバインマークには常にRepositionスクリプトを使用しているので、コンバインマークを重ねても斜体の角度のままです。*

* **Anchor Mover:** 複数のグリフのアンカー位置を一括処理するためのGUI。GUI for batch-processing anchor positions in multiple glyphs. *要Vanilla.*
* **Batch Insert Anchors:** 同名のアンカーを複数のグリフの同一近似位置に一括挿入するためのGUI。GUI for batch-inserting anchors of the same name at the same approximate position in multiple glyphs. *要Vanilla*
* **Find and Replace in Anchor Names:** 選択されたグリフのアンカー名に含まれるテキストを置換するためのGUI。すべてのレイヤーを処理します。GUI for replacing text in the names of anchors in selected glyphs. Processes all layers. *要Vanilla*
* **Fix Arabic Anchor Order in Ligatures:** RTLの*top_X*と*bottom_X*のアンカーの順番を修正しました。異なるフォーマットから変換されたファイルでは、時々 *top_1* が *top_2* の左にあることがあるが、これは逆にすべきで、そうしないと mark2liga が台無しになる。このスクリプトは選択されたグリフを調べ、それがアラビア語の合字であれば、すべてのアンカーをRTL順に並べ替えます。Fixes the order of *top_X* and *bottom_X* anchors to RTL. In files converted from a different format, it sometimes happens that *top_1* is left of *top_2*, but it should be the other way around, otherwise your mark2liga will mess up. This script goes through your selected glyphs, and if they are Arabic ligatures, reorders all anchors to RTL order, at the same time not touching their coordinates.
* **Insert All Anchors in All Layers:** 選択されたグリフの各レイヤー上で、 欠けているアンカーをすべて追加します （ただし、そのグリフの他のレイヤーには存在しています）。アンカーを平均化された位置に配置します。On each layer of a selected glyph, adds all missing anchors (but present in other layers of that glyph). Puts anchors at an averaged position.
* **Insert exit and entry Anchors to Selected Positional Glyphs:** 選択されたグリフの中に、 草書体の添付のための入口と出口のアンカーを追加します。デフォルトでは、出口は (0, 0) に、エントリはそのようなノードが存在する場合には RSB のノードに配置されます。ご自身のニーズに合わせて調整してください。Adds entry and exit anchors for cursive attachment in selected glyphs. By default, it places the exit at (0, 0) and the entry at a node at RSB if such a node exists. Please adjust for your own needs.
* **Mark Mover:** マークをそれぞれの高さに移動させることができます。また、左右のメトリクスキーを設定することもできます。Move marks to their respective heights, e.g. …comb.case to cap height, …comb to x-height, etc. Also allows you to set left and right metrics keys. *要Vanilla*
* **Move ogonek Anchors to Baseline Intersection:** すべての ogonek と _ogonek アンカーを、アウトラインとベースラインの一番右の交点に移動します。Moves all ogonek and _ogonek anchors to the rightmost intersection of the outline with the baseline.
* **Move topright Anchors for Vertical Carons:** topright と _topright のすべてのアンカーを、アウトラインの x-height との交点の一番右に移動する。チェコ語やスロバキア語の文字を縦書きのカロンで作成するのに便利です。Moves all topright and _topright anchors to the rightmost intersection of the outline with the x-height. Useful for building Czech/Slovak letters with vertical caron.
* **Move Vietnamese Marks to top_viet Anchor in Circumflex:** acute*, *grave*, *hookabovecomb* を、選択されたグリフの各レイヤー内の *top_viet* アンカーに移動させます。ベトナム語の二重アクセントに便利。circumflexcomb* のすべてのレイヤーに *top_viet* アンカーがあると仮定する。Moves *acute*, *grave* and *hookabovecomb* to the *top_viet* anchor in every layer of selected glyphs. Useful for Vietnamese double accents. Assumes that you have *top_viet* anchors in all layers of *circumflexcomb*.
* **New Tab with Glyphs Containing Anchor:** 特定のアンカーを含むすべてのグリフで新規タブを開きます。Opens a new tab with all glyphs containing a specific anchor.
* **New Tab with top and bottom Anchors Not on Metric Lines:** すべての *top* と *bottom* アンカーの y 位置をマクロパネルに報告し、フォント内の任意のグリフのマスターレイヤー、ブラケットレイヤー、ブレースレイヤーのいずれかに迷走アンカーを持つすべてのグリフの新しいタブを開きます。ユーザーの選択を無視して、すべてのグリフを分析します。トップアンカーが正確にあるべき位置にないかどうかを調べるのに便利です。Report the y positions of all *top* and *bottom* anchors into the Macro Panel, and opens new tabs with all glyphs that have a stray anchor on any of the master, bracket or brace layers of any glyph in the font. Ignores the user selection, and analyses all glyphs, exporting and non-exporting. Useful to see if a top anchor is not exactly where it should be.
* **Prefix all exit/entry anchors with a hashtag:** フォント内のすべての出口アンカーと入口アンカーを探し、それらのアンカー名の前に `#` を付けて `curs` 機能の生成を無効にします。
* スタッキングアンカーの再調整:**結合アクセントのスタッキングでは、上と下のアンカーを、イタリック体の角度を考慮して、それぞれの _top と _bottom のアンカーの上か下に正確に移動します。このようにして、複数の間隔のない Looks for all exit and entry anchors anywhere in the font, and disables `curs` feature generation by prefixing their anchor names with `#`.
* **Realign Stacking Anchors:** アクセントの組み合わせを重ねる際には、上と下のアンカーを、イタリック体の角度を考慮して、それぞれの_上と_下のアンカーのちょうど上か下に移動させます。この方法では、複数の間隔のないアクセントを重ねても、常に一直線上に収まるようになります。In stacking combining accents, moves top and bottom anchors exactly above or below the respective _top and _bottom anchors, respecting the italic angle. This way, stacking multiple nonspacing accents will always stay in line. *要Vanilla*
* **Remove Anchors in Suffixed Glyphs:** ユーザーが指定したサフィックスのいずれかを持つグリフからすべてのアンカーを削除します。コピー、拡大縮小、編集後にグリフの sups/subs/sinf/ordn バリアントに残っているアンカーを削除するのに便利。Removes all anchors from glyphs with one of the user-specified suffix. Useful for removing left-over anchors in sups/subs/sinf/ordn variants of glyphs after copying, scaling and editing. 
*要Vanilla*
* **Remove Anchors:** 選択されたグリフ（またはフォント全体）の中の指定された名前のアンカーを削除します。Deletes anchors with a specified name in selected glyphs (or the whole font). *要Vanilla*
* **Remove Non-Standard Anchors from Selected Glyphs:** デフォルトでは存在しないはずのグリフからすべてのアンカーを削除します。誤検出を削除する可能性があるので、潜在的に危険である。そこで、まず以下のレポートスクリプトを使用する。Removes all anchors from a glyph that should not be there by default, e.g., `ogonek` from `J`. Potentially dangerous, because it may delete false positives. So, first use the report script below.
* **Replicate Anchors in Suffixed Glyphs:** 選択されたドット接尾辞付きグリフを調べ、それぞれのベースグリフからアンカーを複製します。例えば、*X.ss01*, *X.swsh*, *X.alt*の中の*X*のアンカーを再作成します。Goes through selected dot-suffixed glyphs and duplicates anchors from their respective base glyphs. E.g. will recreate anchors of *X* in *X.ss01*, *X.swsh* and *X.alt*.
* **Report Non-Standard Anchors to Macro window:** フォント内のすべてのグリフを調べ、デフォルト以外のアンカーを見つけた場合にはマクロウィンドウで報告します。編集ビューでは、行はコピーペースト可能です。Goes through all glyphs in the font and reports in the Macro window if it finds non-default anchors. Lines are copy-pasteable in Edit view.

## App（アプリケーション）

*あなたがコーディングをしている場合は、Method Reporterのキーボードショートカットを追加してください。Print Windowは、ウィンドウの内容を解像度に依存しないPDFスクリーンショットを作成したい場合に便利です。ベクターイラストアプリの後処理に最適です。*
*If you are coding, add a keyboard shortcut for Method Reporter, you will need this a lot. Print Window can come in handy if you want a resolution-independent PDF screenshot of your window content. Best for post-processing in a vector illustration app.*

* **Line Height Decrease** and **Line Height Increase:** 編集ビューの行の高さを4分の1ずつ増やしたり、5分の1ずつ減らしたりします。行の高さを何度も切り替える必要がある場合に、ショートカットを設定するのに便利です。Increases the Edit View line height by a quarter, or decreases it by a fifth. Useful for setting shortcuts if you need to switch between line heights a lot.
* **Method Reporter:** Glyphs内から利用できるPythonやPyObjCクラスのメソッド名をフィルタリングするためのGUI。複数のスペースで区切られた検索語（AND連結の場合）とアスタリスクをジョーカー（先頭、中間、末尾）として使用することができます。ダブルクリックでメソッド名をクリップボードに入れ、マクロウィンドウでヘルプを開きます。コーダーに便利です。GUI for filtering through the method names of Python and PyObjC Classes available from within Glyphs. You can use multiple space-separated search terms (for an AND concatenation) and asterisk as jokers (at the beginning, in the middle and at the end). Double click to put the method name in your clipboard and open help in the Macro window. Useful for coders. *要Vanilla*
* **Parameter Reporter:** Method Reporterと似ていますが、カスタムパラメータ用です。ダブルクリックしてクリップボードにパラメータをコピーし、フォント情報に貼り付ける準備ができています。Like Method Reporter, but for custom parameters. Double click to copy a parameter in the clipboard, ready for pasting in Font Info. *要Vanilla*
* **Print Window:** 最前面のウィンドウを印刷します。レポータープラグイン（*View*メニューの拡張機能）のレンダリングを含む、ウィンドウの内容のベクターPDFを保存するのに便利です。Print the frontmost window. Useful for saving a vector PDF of your window content, including the renderings of reporter plug-ins (extensions for the *View* menu).
* **Set Export Paths to Adobe Fonts Folder:** OpenTypeフォントと可変フォントのエクスポートパスをAdobe Fontsフォルダに設定します。Sets the OpenType font and Variable Font export paths to the Adobe Fonts Folder.
* **Set Hidden App Preferences:** GUIには記載されていない「隠れた」アプリの環境設定を読み込んで設定するためのGUI。GUI for reading and setting ‘hidden’ app preferences, which are not listed in the GUI. *要Vanilla*
* **Set Tool Shortcuts:** ツールバーのツールのキーボードショートカットを設定します。Set keyboard shortcuts for the tools in the toolbar. *要Vanilla*
* **Toggle RTL-LTR:** 最前面のタブをLTRとRTLの書き込み方向を切り替えます。システム環境設定でキーボードショートカットを設定するのに便利です。Toggle frontmost tab between LTR and RTL writing direction. Useful for setting a keyboard shortcut in System Preferences.
* **Update git Repositories in Scripts Folder:** Glyphs Scripts フォルダ内のすべてのサブフォルダに対して 'git pull' コマンドを実行します。Scripts フォルダに git repos がたくさんある場合に便利です。Executes a 'git pull' command on all subfolders in the Glyphs Scripts folder. Useful if you have a lot of git repos in your Scripts folder.

## Build Glyphs（グリフ生成）

*最も重要なこと。Quote Manager、および小さい数字、記号、LdotのためのBuildスクリプト。その他のスクリプトは主に、クライアントから要求された場合に、特定のユニコード範囲をカバーするためのクイックスタートを与えることを意図しています。*
*Most important: Quote Manager, and the Build scripts for Small Figures, Symbols, Ldot. The other scripts are mainly intended to give you a quick head start for covering certain Unicode ranges if requested by the client.*

* **Build APL Greek:** APL ギリシャ語のグリフを作成します。Create APL Greek glyphs.
* **Build careof and cadauna:** `c`, `o`, `u`, `fraction` グリフから `cadauna` と `careof` を構築します。Builds `cadauna` and `careof` from your `c`, `o`, `u` and `fraction` glyphs.
* **Build Circled Glyphs:** `part.circle`と文字や図形から丸で囲った数字と文字(U+24B6...24EAとU+2460...2473)を作成します。Builds circled numbers and letters (U+24B6...24EA and U+2460...2473) from `_part.circle` and your letters and figures. *要Vanilla*
* **Build Dotted Numbers:** デフォルトの数字とピリオドから点線の数字を作成します。Build dotted numbers from your default figures and the period.
* **Build Extra Math Symbols:** `lessoverequal`, `greateroverequal`, `bulletoperator`, `rightanglearc`, `righttriangle`, `sphericalangle`, `measuredangle`, `sunWithRays`, `positionIndicator`, `diameterSign`, `viewdataSquare`, `control` をビルドします。Builds `lessoverequal`, `greateroverequal`, `bulletoperator`, `rightanglearc`, `righttriangle`, `sphericalangle`, `measuredangle`, `sunWithRays`, `positionIndicator`, `diameterSign`, `viewdataSquare`, `control`.
* **Build Ldot and ldot:** 既存の `L` と `periodcentered.loclCAT` (`.case`/`.sc`) から `Ldot`, `ldot`, `ldot.sc` をビルドします。すでに `L`-`periodcentered.loclCAT`-`L` などを作成し、適切な間隔をあけていることを前提としています。Builds `Ldot`, `ldot` and `ldot.sc` from existing `L` and `periodcentered.loclCAT` (`.case`/`.sc`). Assumes that you have already created and properly spaced `L`-`periodcentered.loclCAT`-`L`, etc.
* **Build Parenthesized Glyphs:** 括弧付きの文字と数字を作成する。`1.paren`, `two.paren`, `three.paren`, `four.paren`, `five.paren`, `six.paren`, `seven.paren`, `eight.paren`, `nine.paren`, `one_zero.paren`, `one_one. paren`, `one_two.paren`, `one_three.paren`, `one_four.paren`, `one_five.paren`, `one_six.paren`, `one_seven.paren`, `one_eight.paren`, `one_nine.paren`. paren`, `two_zero.paren`, `a.paren`, `b.paren`, `c.paren`, `d.paren`, `e.paren`, `f.paren`, `g.paren`, `h.paren`, `i.paren`, `j.paren`, `k.paren`, `l.paren`, `m.paren`, `m.paren`. パレン`, `m.パレン`, `n.パレン`, `o.パレン`, `p.パレン`, `q.パレン`, `r.パレン`, `s.パレン`, `t.パレン`, `u.パレン`, `v.パレン`, `w.パレン`, `x.パレン`, `y.パレン`, `z.パレン`.Creates parenthesized letters and numbers: `one.paren`, `two.paren`, `three.paren`, `four.paren`, `five.paren`, `six.paren`, `seven.paren`, `eight.paren`, `nine.paren`, `one_zero.paren`, `one_one.paren`, `one_two.paren`, `one_three.paren`, `one_four.paren`, `one_five.paren`, `one_six.paren`, `one_seven.paren`, `one_eight.paren`, `one_nine.paren`, `two_zero.paren`, `a.paren`, `b.paren`, `c.paren`, `d.paren`, `e.paren`, `f.paren`, `g.paren`, `h.paren`, `i.paren`, `j.paren`, `k.paren`, `l.paren`, `m.paren`, `n.paren`, `o.paren`, `p.paren`, `q.paren`, `r.paren`, `s.paren`, `t.paren`, `u.paren`, `v.paren`, `w.paren`, `x.paren`, `y.paren`, `z.paren`.
* **Build Q from O and _tail.Q:** このスクリプトを実行するには、Qテールで*Component from Selection*を行い、`_tail.Q`という名前を付けた後に*実行してください。* Run this script *after* doing *Component from Selection* on the Q tail and naming it `_tail.Q`.
* **Build Rare Symbols:** 白と黒、小と大、円、三角、四角を組み立てます。Builds white and black, small and large, circles, triangles and squares. *要Vanilla*
* **Build Small Figures:** デフォルトの数値集合（例えば，`.dnom`）を受け取り，その他の数値集合（`.numr`, `superior`/`.sups`, `inferior`/`.sinf`, `.subs`）をコンポーネントコピーとして導出します．イタリック体の角度を尊重します。Takes a default set of figures (e.g., `.dnom`), and derives the others (`.numr`, `superior`/`.sups`, `inferior`/`.sinf`, `.subs`) as component copies. Respects the italic angle. *Need Vanilla.*
* **Build small letter SM, TEL:** グリフを作成する。サービスマーク`, `電話`。Creates the glyphs: `servicemark`, `telephone`.
* **Build space glyphs:** `ミディアムスペース-math`, `emquad`, `emspace`, `enquad`, `enspace`, `figurespace`, `fourperemspace`, `hairspace`, `narrownbspace`, `punctuationspace`, `sixperemspace`, `nbspace`, `thinspace`, `threeperemspace`, `zerowidthspace` を作成します。Creates `mediumspace-math`, `emquad`, `emspace`, `enquad`, `enspace`, `figurespace`, `fourperemspace`, `hairspace`, `narrownbspace`, `punctuationspace`, `sixperemspace`, `nbspace`, `thinspace`, `threeperemspace`, `zerowidthspace`.
* **Build Symbols:** `.notdef` (利用可能な最も太字の `question` マークに基づく) や `estimated` グリフ、`bar` や `brokenbar` (標準ステムと斜体角度を尊重する) などのシンボルグリフを作成します。Creates symbol glyphs such as `.notdef` (based on the boldest available `question` mark), an `estimated` glyph, as well as `bar` and `brokenbar` (for which it respects standard stems and italic angle). *要Vanilla*
* **Quote Manager:** シングルクォートからダブルクォートを作成し、自動整列のためにシングルクォートに `#exit` と `#entry` のアンカーを挿入します。シングルクォーテーションはすでに用意しておく必要があります。Build double quotes from single quotes, and insert `#exit` and `#entry` anchors in the single quotes for auto-alignment. You need to have the single quotes already. *要Vanilla*

## Color Fonts（カラーフォント）

*これらのスクリプトは、カラーフォントのワークフローで遭遇するであろう状況のためのものです。Merge スクリプトは主に CPAL/COLR フォントのフォールバックグリフを作成するためのものです。この方法では、フォールバックは完全な bbox を持ち、Chrome でのクリッピングは発生しません。*
*These scripts are for situations you will encounter in a Color Font workflow. The Merge script is mainly for creating a fallback glyph for CPAL/COLR fonts. This way the fallback has the full bbox, and no clipping will occur in Chrome.*

* **Add All Missing Color Layers to Selected Glyphs:** Color Palettes パラメーターで定義されている各 (CPAL/COLR) 色のフォールバックレイヤーの複製を、選択されているグリフごとに追加します。グリフ内にまだない色のみを追加します。Adds a duplicate of the fallback layer for each (CPAL/COLR) color defined in the Color Palettes parameter, for each selected glyph. Only adds colors that are still missing in the glyph.
* **Add sbix Images to Font:** フォルダ内のすべての PNG、GIF、JPG ファイルを取得し、現在のフォントとマスターにそれらのファイルを使って iColor レイヤを作成します。ファイル名の規則: 'glyphname pixelsize.suffix'、例: 'Adieresis 128.png'。Will get all PNG, GIF, JPG files in a folder and create iColor layers with them in the current font and master. File name convention: ‘glyphname pixelsize.suffix’, e.g., ‘Adieresis 128.png’.
* **Convert Layerfont to CPAL+COLR Font:** レイヤー化されたカラーフォントを、各グリフ内にCPAL・COLRレイヤーを持つ単一マスターフォントに変えます。デフォルトでは最初のマスターが使われます。Turns a layered color font into a single-master font with a CPAL and COLR layers in each glyph. It will take the first master as default.
* **Delete Non-Color Layers in Selected Glyphs:** タイプ「Color X」以外のグリフ（CPAL/COLR レイヤ）のすべてのサブレイヤを削除します。Deletes all sublayers in all glyphs that are not of type "Color X" (CPAL/COLR layers).
* **Merge All Other Masters in Current Master:** 選択されたグリフにおいて、他のマスターからのすべてのパスを現在のマスターレイヤーにコピーします。In selected glyphs, copies all paths from other masters onto the current master layer.
* **Merge Suffixed Glyphs into Color Layers:** x.shadow、x.body、x.frontをxの別個のCPALカラーレイヤーにマージします。Merges x.shadow, x.body and x.front into separate CPAL Color layers of x. *要Vanilla*
* **sbix Spacer:** sbix の位置とグリフ幅を一括設定します。Batch-set sbix positions and glyph widths. *要Vanilla*

## Compare Frontmost Fonts(フォントの比較)

*これらのスクリプトは、アップライトをイタリック体と同期させるためのものです。2つのフォントを開き、スクリプトを実行します。フォントは変更されませんが、マクロウィンドウで詳細を報告します。*
*These scripts are intended for syncing uprights with their italics. Open two fonts, and run the scripts. They do not change your fonts, but report in detail in the Macro window.*

* **Compare Font Info > Font:** 最前列の2つのフォントについて、フォント情報 > フォントの詳細レポートを作成し、マクロウィンドウにレポートを出力します。Detailed report of Font Info > Masters for the two frontmost fonts and outputs a report in the Macro window.
* **Compare Font Info > Masters:** 最前列の2つのフォントについて、フォント情報 > マスターズの詳細レポートを作成し、マクロウィンドウにレポートを出力します。Detailed report of Font Info > Masters for the two frontmost fonts and outputs a report in the Macro window.
* **Compare Font Info > Instances:** 最前面の2つのフォントについて、フォント情報 > インスタンスの詳細レポートを作成し、マクロウィンドウにレポートを出力します。Detailed report of Font Info > Instances for the two frontmost fonts and outputs a report in the Macro window.
* **Compare Font Info > Features:**  最前面の2つのフォントのOT機能セットを比較し、マクロウィンドウにレポートを出力します。Compares the OT features set of the two frontmost fonts and outputs a report in the Macro window.
* **Compare Anchors:** 最前面の2つのフォント間のアンカー構造とアンカーの高さを比較します。Compares anchor structure and anchor heights between the two frontmost fonts.
* **Compare Composites:** 例えば、あるフォントでは `acutecomb` と一緒に `iacute` が構築され、別のフォントでは `acutecomb.narrow` が構築されているなど、複合グリフの構成要素の構造が異なっていることを報告しています。Reports diverging component structures of composite glyphs, e.g., `iacute` built with `acutecomb` in one font, and `acutecomb.narrow` in the other.
* **Compare Glyph Heights:** 2 番目のフォントと高さが異なるすべてのグリフを、与えられた閾値を超えて一覧表示します。Lists all glyphs that differ from the second font in height beyond a given threshold.
* **Compare Glyph Info:** オープンフォントを比較し、Unicode 値や分類を含む異なるグリフ情報のリットを構築します。Compares open fonts and builds a lits of differing glyph info, including Unicode values and categorisation. *要Vanilla*
* **Compare Glyphsets:** 最前面の 2 つのフォントのグリフセットを比較し、マクロウィンドウにレポートを出力します。Compares the glyph set of the two frontmost fonts and outputs a report in the Macro window.
* **Compare Kerning Groups:** 最前面のフォント間のカーニンググループを比較し、グループが一致しないグリフ名の表を出力します。Compares kerning groups between frontmost fonts, outputs a table of glyph names with unmatching groups.
* **Compare Metrics:** 最前面の2つのフォントの幅を比較します。Compare widths of two frontmost fonts.
* **Compare Sidebearings:** 最前面の2つのフォントのサイドベアリングを比較します。Compare sidebearings of two frontmost fonts.

## Components（コンポーネント）

*コンポーネントで背景をポップレートするは、他のものに基づいて文字を構築するときに非常に便利です、例えば、aeやoeは背景にeを取ることができます。スクリプトは各マスターの背景にeを配置し、UIには選択したポイントを背景のeに合わせるオプションがあります。複数のマスターフォントでセリフにコーナーコンポーネントを使う場合、Propagateスクリプトは多くの時間を節約してくれます。*
*Populate Backgrounds with Components is very useful when you build letters based on other, e.g., ae or oe can take an e in the background. The script puts the e in the background of each master, and the UI has an option to align selected points with the e in the background. If you use corner components for serifs in a multiple-master font, the Propagate script will save you a lot of time.*

* **Alignment Manager:** 選択されたグリフの可視レイヤー上のすべての構成要素の自動整列を有効または無効にします。コンテキストメニューのコマンドと同じですが、多くのグリフに対して一度に行うことができます。Enables or disables automatic alignment for all components on visible layers in selected glyphs. Does the same as the command in the context menu, but you can do it in one step for many glyphs. *要Vanilla*
* **Decompose Components in Background:** 選択されたグリフの背景レイヤーを分解します。現在のマスターでのみ動作します。Decomposes background layers of selected glyphs. Only works on the current master.
* **Decompose Corner and Cap Components:** 選択されたグリフ内のすべての角とキャップの成分を分解します。マクロウィンドウにレポートします。Decomposes all corner and cap components in selected glyphs. Reports to Macro window.
* **Find and Replace Components:** 選択されたグリフ内の構成要素を新しいソースグリフにリンクします。Relinks components in selected glyphs to a new source glyph. *要Vanilla*
* **Find and Replace Cap and Corner Components:** 選択されたグリフ内の `_cap.*` と `_corner.*` コンポーネントを別のコーナー/キャップコンポーネントにリンクします。Relinks `_cap.*` and `_corner.*` components in selected glyphs to a different corner/cap component. *要Vanilla*
* **Find and Replace Corner Components at Certain Angles:** 鈍角または鋭角のコーナーコンポーネントを交換します。Replace Corner Components at blunt or acute angles. *要Vanilla*
* **New Tab with Composable Glyphs that have no Components:** パスで構成されているが、グリフデータに従って構成されている可能性のあるすべてのグリフを含む新しい編集タブを開きます。Opens a new Edit tab containing all glyphs that consist of paths, but could be composed according to Glyph Data.
* **New Tab with Detached Corner Components:** ノードに適切に接続されていないコーナーコンポーネントを持つすべてのグリフを含む新しい編集タブを開きます。Opens a new Edit tab containing all glyphs that have a corner component which is not properly connected to a node.
* **New Tab with Locked Components:** ロックされたコンポーネントを含むすべてのレイヤーを含む新しいタブを開きます。Opens a new tab containing all layers that contain locked components.
* **New Tab with Orphaned Components:** 存在しないグリフ、すなわちベースグリフがないグリフを指す成分を持つすべてのグリフ（カレントマスターの）を含む、カレントフォントウィンドウ内の新しいタブを開きます。Opens a new tab in the current font window containing all glyphs (of the current master) that have components that point to non-existent glyphs, i.e., no base glyphs.
* **New Tab with Transformed Components:** ミラーリング、シフト、回転、スケーリングされた成分を持つすべての複合グリフを含む新しいタブを開きます。Opens a new tab containing all compound glyphs that have mirrored, shifted, rotated, or scaled components. *要Vanilla*
* **New Tab with Transformed Corner Components:** Opens a new Edit tab containing all glyphs with scaled corner components.

* **New Tab with Unusual Compounds:** 誤った成分の順序を持っているか、または正統でない成分構造を持っているすべての複合グリフを含む新しいタブを開きます。誤った成分順を見つけるのに便利です。Open a new tab containing all compound glyphs that have an unusual component order or an unorthodox component structure. Useful for finding wrong component orders.
* **Populate Backgrounds with Components:** すべてのグリフまたは選択されたすべてのグリフから指定された成分を削除します。Removes the specified component from all glyphs or all selected glyphs. *要Vanilla*
* **Propagate Corner Components to Other Masters:** 同じグリフの他のすべてのマスターの中で、 カレントマスターレイヤーの角の成分を再現しようとします。アウトラインが互換性のあるものであることを確認してください。Tries to recreate the corner components of the current master layer in all other masters of the same glyph. Make sure your outlines are compatible.
* **Remove Components:** すべての（選択された）グリフから指定された成分を削除します。Removes the specified component from all (selected) glyphs.
* **Stitcher:** 選択されたグリフの中で、 スティッチャは一定の間隔でパス上に成分を挿入します。開いたパス (モノライン) を点線にするのに便利です。原点」と呼ばれるアンカーを使って、 ステッチされた文字の中の構成要素の位置を決定します。In selected glyphs, the Stitcher inserts components on your paths at fixed intervals. Useful for turning open paths (monolines) into dotted lines. Use an anchor called 'origin' for determining the component position in stitched letters. *要Vanilla*
* **Sync Components Across Masters:** 現在のレイヤーのコンポーネントを取り、他のすべてのマスターを同じコンポーネント構造にリセットします。パスとアンカーを無視します。Optionキーを押しながら、すべてのパスとアンカーを *delete* します。Takes the current layer’s components, and resets all other masters to the same component structure. Ignores paths and anchors. Hold down Option key to *delete* all paths and anchors.

## Features(フィーチャー機能)


*スクリプト書体では、Build Positional caltスクリプトが必要になることがよくあります。OT機能のオン/オフを頻繁に行う場合は、Activate Default FeaturesとFloating Featuresスクリプトを参照してください。また、Window > Plugin ManagerのSet Paletteをチェックしてみてください。*
*In script typefaces, you may often need the Build Positional calt script. If you find yourself turning OT features on and off a lot, take a look at the Activate Default Features and Floating Features scripts. And check out the Set Palette from Window > Plugin Manager.*

* **Activate Default Features:** 現在の編集タブでは、デフォルトでオンにすることが推奨されているすべてのOT機能を有効にします（仕様によると）。In the current Edit tab, activates all OT features that are recommended to be on by default (according to the spec).
* **Build Italic Shift Feature:** シフティンググリフ用の GPOS 機能コードを作成して挿入します。Creates and inserts GPOS feature code for shifting glyphs, e.g., parentheses and punctuation for the case feature. *要Vanilla*
* **Build Positional calt Feature:** .init, .medi, .fina, .isolグリフを探し、位置置換コードをcalt機能に注入します。再度実行すると、そのクラスとフィーチャのコードが更新されます。詳細はこのチュートリアルを参照してください: https://glyphsapp.com/tutorials/features-part-4-positional-alternates。Looks for .init, .medi, .fina, and .isol glyphs, and injects positional substitution code into your calt feature. If run again, will update its class and feature code. See this tutorial for more info: https://glyphsapp.com/tutorials/features-part-4-positional-alternates
* **Build rand Feature:** .cvXX または別の（番号付きの）サフィックスから，ランダムな（ランダムな）特徴量を構築します．Build rand (random) feature from .cvXX or another (numbered) suffix. *要Vanilla*
* **Feature Code Tweaks:** OT機能のコードに微調整を追加しました。マクロウィンドウでレポートします。注意: オプションを理解できない場合は使用しないでください。Adds tweaks to OT feature code. Reports in Macro window. Careful: if you do not understand an option, do not use it. *要Vanilla*
* **Find in Features:** OTの機能、接頭辞、クラスで式（グリフ、ルックアップ、クラス名）を検索します。Finds expressions (glyph, lookup or class names) in OT Features, Prefixes and Classes. *要Vanilla*
* **Floating Features:** OT 機能の有効化と無効化のためのフローティングパレット。ポップアップメニューと同じ機能。Floating palettes for activating and deactivating OT features. Same functionality as the pop-up menu. *要Vanilla*
* **Fraction Fever 2:** フォントにTal Lemingのフラクションフィーバー2のコードを挿入します。詳しくはこのチュートリアルをご覧ください: https://glyphsapp.com/tutorials/fractions Insert Tal Leming’s Fraction Fever 2 code into the font. Read more in this tutorial: https://glyphsapp.com/tutorials/fractions
* **New OT Class with Selected Glyphs:** 選択されたグリフで新しいOTクラスを作成するためのGUI。GUI for creating a new OT class with the selected glyphs. *要Vanilla*
* **New Tab with OT Class:** OTクラス(*File > Font Info > Features > Classes*にリストされている)のすべてのグリフを新しいタブで開くためのGUI。GUI for opening all glyphs in an OT class (listed in *File > Font Info > Features > Classes*) in a new tab. *要Vanilla*
* **Update Features without Reordering:** フォント内の既存の機能を調べて、それぞれの機能を更新します。機能の追加や並び替えはしません。Goes through the existing features in the font and refreshes each one of them. Does neither add nor reorder features.
* * **Stylistic Sets > Synchronize ssXX glyphs:** 欠落している ssXX グリフを作成して、同期した ssXX グリフのグループを作成します。例えば、*a.ss01 b.ss01 c.ss01 a.ss02 c.ss02* があるとすると、スクリプトは*b.ss02* を作成します。Creates missing ssXX glyphs so that you have synchronous groups of ssXX glyphs. E.g. you have *a.ss01 b.ss01 c.ss01 a.ss02 c.ss02* --> the script creates *b.ss02*
* * **Stylistic Sets > Create ssXX from layer:** カレントレイヤーを取り、それを新しい .ssXX グリフのプライマリレイヤーにコピーします。Takes the current layer and copies it to the primary layer of a new .ssXX glyph.
* * **Stylistic Sets > Create pseudorandom calt feature:** フォント内の既存の ssXX グリフの数に基づいて、擬似ランダムカルト (文脈上の代替) 機能を作成します。また、回転アルゴリズムにデフォルトクラスも含まれています。Creates pseudorandom calt (contextual alternatives) feature based on number of existing ssXX glyphs in the font. Also includes the default class in the rotation algorithm.
* * **Stylistic Sets > Set ssXX Names:** ssXX 機能の名前を、'Alternate' または他の選ばれたテキス ト に加えて、最初に置き換えられたグリフの名前、例えば 'Alternate a' をプリフィルします。既存の名前を保持するためのオプション。Prefills names for ssXX features with ‘Alternate’ or another chosen text, plus the name of the first substituted glyph, e.g., ‘Alternate a’. Option to preserve existing namings.*要Vanilla*

## Font Info(フォント情報)

*「フォント情報 > フォント」と「フォント情報 > マスター」で垂直メトリックパラメータを検索して同期させるのに便利です。Clean Version Stringも非常に便利です。Font Info Batch Setterは、多くのフォント間でFont Infoの設定を同期するために必要です。WWS/Preferred Namesスクリプトの設定に注意。通常、このアプリは自動的に命名の世話をするので、それらの使用例は非常にまれです。*
*Vertical Metrics is useful for finding and syncing the vertical metric parameters in Font Info > Font and Font Info > Masters. Clean Version String is very useful too. Font Info Batch Setter is a must for syncing Font Info settings across many fonts. Careful about Set WWS/Preferred Names scripts: The app usually takes care of naming automatically, so their use cases are very rare.*

* **Clean Version String:** クリーンな versionString パラメータを追加し、バージョン文字列中の ttfAutohint 情報を無効化した。エクスポートされたフォントは、'Version X.XXX' のみからなるバージョン文字列を持つようになる。Adds a clean versionString parameter, and disables ttfAutohint info in the version string. The exported font will have a version string consisting only of ‘Version X.XXX’.
* **Find and Replace in Font Info:** *フォント情報 > フォント*および*フォント情報 > インスタンス*で名前を検索して置換します。Finds and replaces names in *Font Info > Font* and *Font Info > Instances.* *要Vanilla*
* **Find and Replace In Instance Parameters:** 現在のフォントまたはプロジェクトファイルの選択されたインスタンスをカスタムパラメータで検索して置換します。Finds and Replace in Custom Parameters of selected instances of the current font or project file.
* **Font Info Batch Setter:** *フォント情報 > フォント*の設定を一括適用してフォントを開く：デザイナー、デザイナーURL、メーカー、メーカーURL、著作権、バージョン番号、日時。多くのフォント間でフォント情報の設定を同期するのに便利です。Batch-apply settings in *Font Info > Font* to open fonts: designer, designer URL, manufacturer, manufacturer URL, copyright, version number, date and time. Useful for syncing Font Info settings across many fonts. *要Vanilla*
* **Font Info Overview:** 開いているすべてのフォントのフォント情報の値を一覧表示します。Lists some Font Info values for all opened fonts.
* **Remove Custom Parameters:** フォント情報 > フォント、マスター、インスタンスから1種類のすべてのパラメータを削除します。多くのマスターやインスタンスがある場合に便利です。Removes all parameters of one kind from Font Info > Font, Masters, Instances. Useful if you have many masters or instances. *要Vanilla*
* **Set Preferred Names (Name IDs 16 and 17)  for Width Variants:** すべてのインスタンスにPreferred Namesカスタムパラメータ（名前ID 16と17）を設定し、Adobeアプリ内の別メニューに幅のバリアントが表示されるようにします。Sets Preferred Names custom parameters (Name IDs 16 and 17) for all instances, so that width variants will appear in separate menus in Adobe apps. 
* **Set Style Linking:** Attempts to set the Bold/Italic bits.
* **Set Subscript and Superscript Parameters:** 優劣数値を測定し、下付き文字/上付き文字のX/Yオフセット/サイズパラメータを導出します。Measures your superior and inferior figures and derives subscript/superscript X/Y offset/size parameters. *要Vanilla*
* **Set WWS Names (Name IDs 21 and 22):** 必要に応じてすべてのインスタンスにWWSカスタムパラメータ(名前ID 21と22)を設定します。RIBBI 以外のすべての情報を WWSFamilyName に入れ、WWSSubfamilyName の RIBBI だけを保持します。Sets WWS custom parameters (Name IDs 21 and 22) for all instances where necessary: Puts all info except RIBBI into the WWSFamilyName, and only keeps RIBBI for the WWSSubfamilyName. 
* **Style Renamer:** スタイル名に名前パーティクルを一括で追加したり、一括で削除したりできます。すべてのスタイルをイタリック体からローマ字体に切り替えたり、その逆の場合に便利です。Batch-add a name particle to your style names, or batch-remove it from them. Useful for switching all your styles from italic to roman naming and vice versa. *要Vanilla*
* **Vertical Metrics Manager:** OS/2 usWinとsTypo、hhea、fsSelectionビット7の値を計算して挿入します（usWinのメトリクスよりもsTypoのメトリクスを優先するため）。Calculate and insert values for OS/2 usWin and sTypo, hhea and fsSelection bit 7 (for preferring sTypo Metrics over usWin metrics). *要Vanilla*

## Glyph Names, Notes and Unicode(グリフ名、ノート、Unicode)

*ほとんどのスクリプトは、グリフ名やユニコードの管理を少し簡単にしてくれます。Garbage Collectionは、ファイルを第三者に渡す前に、レポータースクリプトや他の注釈の混乱を一掃するのに便利です。*
*Most scripts make managing glyph names and Unicodes a little easier. Garbage Collection is useful for cleaning up the mess of the reporter scripts, or other annotations before you hand the files over to a third party.*

* **Add PUA Unicode Values to Selected Glyphs:** 選択されたグリフを順次処理し、ユーザーが指定した値から順にカスタム Unicode 値を適用していきます。Iterates through selected glyphs and incrementally applies custom Unicode values, starting at a user-specified value. *要Vanilla*
* **Convert to Uppercase:** 小文字の名前を大文字の名前に変換します。Turns lowercase names into uppercase names, e.g., `a` → `A`, `ccaron` → `Ccaron`, `aeacute` → `AEacute`, etc.
* **Convert to Lowercase:** 選択したグリフの名前を小文字にします。Turns the names of selected glyphs lowercase.
* **Encoding Converter:** インポート/エクスポート可能なテキストをベースに、古いエキスパートの8ビットエンコーディングをGlyphsナイスネームに変換します。デフォルトはAXt変換スキームです。Converts old expert 8-bit encodings into Glyphs nice names, based on a importable/exportable text with renaming scheme. Default is an AXt converting scheme. *要Vanilla*
* **Garbage Collection:** ノード名、グリフ名、注釈などのグリフ内のマーカーやガイドを削除します。Removes markers in glyphs, such as node names, glyph names or annotations, as well as guides.
* **New Tab with Uppercase-Lowercase Inconsistencies:** 大文字小文字の一貫性のないすべてのグリフを含む新しい編集タブを開きます。マクロウィンドウに詳細なレポートを書き込みます。Opens a new Edit tab containing all glyphs without consistent case folding. Writes a detailed report in Macro Window.
* **Production Namer:** デフォルトのプロダクション名を上書きします。デフォルトは、レガシーPDFワークフローで問題を生んでいる通常の主題です。Override default production names. Default are the usual subjects which create problems in legacy PDF workflows: mu, onesuperior, twosuperior, threesuperior. *要Vanilla*
* **Rename Glyphs:** `oldglyphname=newglyphname` のペアのリストを受け取り、それに応じてフォント内のグリフを *Rename Glyphs* カスタムパラメータと同じようにリネームします。Takes a list of `oldglyphname=newglyphname` pairs and renames glyphs in the font accordingly, much like the *Rename Glyphs* custom parameter. *要Vanilla*
* **Reorder Unicodes of Selected Glyphs:** デフォルトの Unicode が先に来るようにユニコードを並べ替えます。Reorders Unicodes so that default Unicode comes first.

## Guides(ガイド)

*これらのスクリプトは、サードパーティ製フォントで作業しているときに目にするたくさんのガイドを一掃することを主な目的としています。*
*These scripts are mostly intended for cleaning up the plethora of guides I see when working on third-party fonts.*

* **Guides through All Selected Nodes:** 現在のグリフ内で選択されているすべてのノードにガイドを敷き詰めます。ガイドの重複を避けるようにしています。Lays guides through all selected nodes in current glyph. Tries to avoid duplicate guides.
* **Remove Global Guides in Current Master:** 現在のマスターのグローバル（赤）ガイドをすべて削除します。Deletes all global (red) guides in the current master.
* **Remove Local Guides in Selected Glyphs:** 選択されたグリフのローカル(青)ガイドをすべて削除します。Deletes all local (blue) guides in selected glyphs.
* **Select All Local Guides:** すべてのローカル（青）ガイドを選択します（選択されているすべてのグリフ内）。Selects all local (blue) guides (in all selected glyphs).

## Hinting（ヒント）

*最も重要なこと: blueScaleを設定し、PostScriptヒントのファミリーアライメントゾーンを設定します。大きな変更を行う場合は、TransferスクリプトとKeep Onlyスクリプトを使用すると、多くの作業を省くことができます。新しいタブスクリプトは、ゾーンのないグリフを見つけるのに役立ちます。また、この目的のために Paths > Near Vertical Misses を検討してみてください。*
*Most important: Set blueScale, Set Family Alignment Zones for PostScript hinting. If you are making big changes, The Transfer and Keep Only scripts can save you a lot of work. The New Tab scripts help find glyphs missing zones. Also consider Paths > Find Near Vertical Misses for that purpose.*

* **Add Alignment Zones for Selected Glyphs:** すべてのマスターで選択されたグリフにフィットゾーンを作成します。Creates fitting zones for the selected glyphs in all masters. *要Vanilla*
* **Add Hints for Selected Nodes:** 選択されたノードのヒントを追加します。ゾーン内のノードが正確に1つ選択されている場合、ゴーストヒントを追加します。システム環境設定でショートカットを設定するのに便利です。Adds hints for the selected nodes. Tries to guess whether it should be H or V. If exactly one node inside a zone is selected, it will add a Ghost Hint. Useful for setting a shortcut in System Prefs.
* **Add TTF Autohint Control Instructions for Current Glyph:** 現在のインスタンスの制御命令に、指定されたアップ/ダウン量のタッチ・ラインを追加します。Adds a touch line for a given up/down amount to the Control Instructions of the current instance. *要Vanilla*
* **BlueFuzzer:** すべての整列ゾーンを指定した値だけ拡張します。blueFuzz の値が使用されていたのと似ているので、この名前が付けられました。Extends all alignment zones by the specified value. Similar to what the blueFuzz value used to do, hence the name. *要Vanilla*
* **Keep Only First Master Hints:** 選択されたグリフにおいて、最初のマスターとして順序づけられたものを除いて、すべてのレイヤー内のすべてのヒントを削除します。ブラケットレイヤを尊重します。例えば、最初のマスターが 'Regular' の場合、スクリプトは 'Bold'、'Bold [120]' のヒントを削除しますが、'Regular' と 'Regular [100] のヒントは保持します。In selected glyphs, deletes all hints in all layers except for whatever is ordered as first master. Respects Bracket Layers. E.g., if your first master is 'Regular', then the script will delete hints in 'Bold', 'Bold [120]', but keep them in 'Regular' and 'Regular [100]'.
* **New Tab with Glyphs in Alignment Zones:** 新しいタブを開き、アライメントゾーンに到達するすべてのグリフを一覧表示します。Opens a new tab and lists all glyphs that reach into alignment zones.
* **New Tabs with Glyphs Not Reaching Into Zones:** 上にも下にも位置合わせゾーンに届かないすべてのグリフを含む新しいタブを開きます。現在のマスターにパスを含むグリフのみをカウントします。空のグリフや化合物は無視します。Opens a new tab with all glyphs that do NOT reach into any top or bottom alignment zone. Only counts glyphs that contain paths in the current master. Ignores empty glyphs and compounds. *要Vanilla*
* **Remove PS Hints:** カ レ ン ト フ ォ ン ト 、 選択 さ れてい る マ ス タ ー、 選択 さ れてい る グ リ フ のいずれかにあ る 幹やゴーストのヒントをすべて削除 し ます。Deletes all stem and/or ghost hints throughout the current font, the selected master and/or the selected glyphs. *要Vanilla*
* **Remove TT Hints:** カレントフォント、選択されているマスター、および/または選択されているグリフ全体に渡って、ユーザーが指定したTT命令のセットを削除します。Deletes a user-specified set of TT instructions throughout the current font, the selected master and/or the selected glyphs. *要Vanilla*
* **Remove Zero Deltas in Selected Glyphs:** 選択された各グリフのすべてのレイヤーを通過し、オフセットがゼロのすべての TT デルタヒントを削除します。マクロウィンドウの詳細レポート。Goes through all layers of each selected glyph, and deletes all TT Delta Hints with an offset of zero. Detailed Report in Macro window.
* **Set blueScale:** フォント情報 > フォントで可能なblueScaleの最大値（オーバーシュート抑制のための最大サイズの決定）を設定します。マクロウィンドウで他のオプションを出力します。Sets maximum blueScale value (determining max size for overshoot suppression) possible in Font Info > Font. Outputs other options in Macro window.
* **Set Family Alignment Zones:** インスタンスをピックして、そのゾーンをファミリー整列ゾーンとして *フォント情報 > フォント > カスタムパラメータ* で設定します。Pick an instance and set its zones as Family Alignment Zones in *Font Info > Font > Custom Parameters.* *要Vanilla*
* **Set TT Stem Hints to Auto:** 選択されたグリフ内のすべての TT ステムヒントを「自動」に設定します。Sets all TT stem hints to ‘auto’ in selected glyphs.
* **Set TT Stem Hints to No Stem:** 選択されたグリフのすべてのTTステムヒントを「ステムなし」に設定します。複雑なパスでは、Windows上でのレンダリングを向上させることができます。Sets all TT stem hints to ‘no stem’ in selected glyphs. In complex paths, it can improve rendering on Windows.
* **Set TTF Autohint Options:** 既存の「TTF Autohint Options」カスタムパラメータのオプションを設定します。Set options for existing 'TTF Autohint Options' Custom Parameters. *要Vanilla*
* **Transfer Hints to First Master:** パスが互換性のあるものであれば、現在のレイヤーから最初のマスターレイヤーにPSヒントをコピーします。エラーをマクロウィンドウに報告します。Copies PS hints from the current layer to the first master layer, provided the paths are compatible. Reports errors to the Macro window.
* **TT Autoinstruct:** 選択されたマスターの中の選択されたグリフに自動的に Glyphs TT 命令を追加する。(最初のマスターでなければなりません。) 注意: これは Werner Lemberg の ttfAutohint ではなく、TT 命令ツール (I) が同名のコンテキストメニュー項目を使って追加する手動の TT ヒントです。一度に多くのグリフにヒントを追加するのに便利です。Automatically add Glyphs TT instructions to the selected glyphs in the selected master. (Should be the first master.) Attention: this is NOT Werner Lemberg's ttfAutohint, but the manual TT hints that the TT Instruction tool (I) would add through the context menu item of the same name. Useful for adding hints in many glyphs at once.

## Images(画像)

*主に（背景）画像を多く扱う際に起こる頭痛を治すことを目的としています。*
*Mainly intended for curing the headaches you may undergo when handling a lot of (background) images.*

* **Add Same Image to Selected Glyphs:** 画像を要求し、それを背景画像として現在選択されているすべてのグリフに挿入します。Asks you for an image, and then inserts it into all currently selected glyphs as background image.
* **Adjust Image Alpha:** 選択したグリフ内の全画像のアルファ値を設定するためのスライダー。Slider for setting the alpha of all images in selected glyphs. *要Vanilla*
* **Delete All Images in Font:** フォント全体に配置された画像をすべて削除します。Deletes all placed images throughout the entire font.
* **Delete Images:** 選択されているグリフの可視レイヤーに配置されているすべての画像を削除します。Deletes all images placed in the visible layers of selected glyphs.
* **Reset Image Transformation:** 選択されたグリフの可視レイヤーにおいて、すべての画像変換 (x/y オフセット、縮尺、歪み) をデフォルトに戻します。Resets all image transformations (x/y offset, scale, and distortion) back to default in the visible layers of selected glyphs.
* **Set New Path for Images:** 選択されたグリフ内に配置された画像のパスをリセットします。画像を移動した場合に便利です。Resets the path for placed images in selected glyphs. Useful if you have moved your images.
* **Toggle Image Lock:** 選択されているすべてのグリフのすべての画像をロックまたはロック解除します。Lock or unlock all images in all selected glyphs. *要Vanilla*
* **Transform Images:** 選択したグリフの可視レイヤー内の画像（x/y オフセットと x/y スケール）をバッチ変換するための GUI。GUI for batch-transforming images (x/y offset and x/y scale) in the visible layers of selected glyphs. *要Vanilla*

## Interpolation(補間)

*最も重要なのは、インスタンスの挿入（インスタンスとそのスタイルのリンクを決定するため）、Kink Finder、シェイプシフトグリフの検索です。私はキーボードショートカットのctrl-up/downで次のインスタンス/前のインスタンスを表示するのをよく使っています。*
*Most important: Insert Instances (for determining your instances and their style linking), Kink Finder and Find Shapeshifting Glyphs. I use Show Next/Previous Instance with the keyboard shortcut ctrl-up/down a lot.*

* **Axis Mapper:** Axis Mappings パラメータの「avar」軸マッピングを抽出、リセット、および挿入します。Extracts, resets and inserts an ‘avar’ axis mapping for the Axis Mappings parameter. *要Vanilla*
* **Composite Variabler:** ブレース層とブラケット層が使用されている化合物中のコンポーネントを再複製します。ブラケット層をコンポジットで機能させます。Reduplicates Brace and Bracket layers of components in the compounds in which they are used. Makes bracket layers work in composites. *要Vanilla*
* **Copy Layer to Layer:** あるマスターから別のマスターへパス（オプションでコンポーネント、アンカー、メトリクスも）をコピーします。Copies paths (and optionally, also components, anchors and metrics) from one Master to another. *要Vanilla*
* **Dekink Masters:** 互換性のあるすべてのレイヤーでスムーズな点の三重項をデキンクします（水平または垂直でない場合に便利です）。1 つ以上の滑らかな点の三重項で点を選択し、このスクリプトを実行して他のすべてのマスターの対応するノードを同じ相対位置に移動させます。このようにして、すべてのマスターで同じ点の比率を達成し、トリプレットの角度が変化したときの補間キンクを回避することができます。これを説明したビデオがあります](http://tinyurl.com/dekink-py) トリプレット問題は、このチュートリアルで説明されています](http://www.glyphsapp.com/tutorials/multiple-masters-part-2-keeping-your-outlines-compatible)。Dekinks your smooth point triplets in all compatible layers (useful if they are not horizontal or vertical). Select a point in one or more smooth point triplets, and run this script to move the corresponding nodes in all other masters to the same relative position. Thus you achieve the same point ratio in all masters and avoid interpolation kinks, when the angle of the triplet changes. There is a [video describing it.](http://tinyurl.com/dekink-py) The triplet problem is [described in this tutorial](http://www.glyphsapp.com/tutorials/multiple-masters-part-2-keeping-your-outlines-compatible).
* **Fill up Empty Masters:** あるマスターから別のマスターにパスをコピーします。ただし、ターゲットマスターが空の場合に限ります。Copies paths from one Master to another. But only if target master is empty. *要Vanilla*
* **Find and Replace in Layer Names:** 選択されたグリフのすべてのレイヤー名 (マスターレイヤーを除く) の中のテキストを置き換えます。多くのグリフで括弧トリックを使っている場合に便利です。Replaces text in all layer names (except Master layers) of selected glyphs. Useful if you use the bracket trick in many glyphs. *要Vanilla*
* **Find Shapeshifting Glyphs:** 補間中にパスの数が変わるグリフを見つけます。新しいタブを開き、マクロウィンドウにレポートします。Finds glyphs that change the number of paths while interpolating. Opens a new tab and reports to Macro window. *要Vanilla*
* **Insert Brace Layers for Component Rotation:** 連続的にスケールされ、回転したコンポーネントを持つ複数のブレースレイヤーを挿入します。回転要素を使った OTVar 補間に便利です。Inserts a number of Brace Layers with continuously scaled and rotated components. Useful for OTVar interpolations with rotating elements. *要Vanilla*
* **Insert Brace Layers for Movement along Background Path:** 背景の最初のパスに応じてシフトされた最初のレイヤーのコピーを持つ複数のブレースレイヤーを挿入します。移動する要素を使った OTVar 補間に便利です。Inserts a number of Brace Layers with copies of the first layer, shifted according to the first path in the background. Useful for OTVar interpolations with moving elements.
* **Insert Instances:** ウェイトインスタンスを計算して挿入するためのGUI。このチュートリアルで説明しています: https://www.glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances GUI for calculating and inserting weight instances. It is described in this tutorial: https://www.glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances *要Vanilla*
* **Insert Layers:** 選択したグリフの中にブレースまたはブラケットレイヤーを一括挿入します。Batch-insert brace or bracket layers in selected glyphs. *要Vanilla*
* **Kink Finder:** アウトラインや補間空間のキンクを見つけ、マクロウィンドウで報告し、影響を受けたグリフで新しいタブを開きます。キンクについてはこのチュートリアルで説明しています: https://glyphsapp.com/tutorials/multiple-masters-part-2-keeping-your-outlines-compatibleFinds kinks in outlines or the interpolation space, reports them in the Macro window and opens a new tab with affected glyphs. Kinks are described in this tutorial: https://glyphsapp.com/tutorials/multiple-masters-part-2-keeping-your-outlines-compatible *要Vanilla*
* **New Tab with Dangerous Glyphs for Interpolation:** 互換性のある要素を 2 つ以上含むフォント内のすべてのグリフのタブを開きます。すなわち、等号のように、ある要素（パスやコンポーネント）が間違った要素と補間してしまう可能性のあるグリフ。詳細な説明は、このチュートリアルの *Be suspicious* を参照してください。<http://www.glyphsapp.com/tutorials/multiple-masters-part-2-keeping-your-outlines-compatible> を参照してください。Opens a tab with all glyphs in the font that contain at least two compatible elements. I.e., glyphs where an element (a path or a component) could interpolate with the wrong element, like the equals sign. For a detailed description, see section *Be suspicious* in this tutorial: <http://www.glyphsapp.com/tutorials/multiple-masters-part-2-keeping-your-outlines-compatible>.
* **New Tab with Special Layers:** 中括弧レイヤと括弧レイヤを含むすべてのグリフを含む新しい編集タブを素早く追加します。Quickly adds a new edit tab with all glyphs containing brace and bracket layers.
* **New Tab with Uneven Handle Distributions:** ハンドルの分布が大きく変化しているグリフを見つけます（例：バランスから調和へ）。Finds glyphs where handle distributions change too much (e.g., from balanced to harmonised). *要Vanilla*
* **OTVar Player:** カレントグリフを、ウェイト軸に沿ったループでアニメーション化します。Animates the current glyph with a loop along the weight axis. *要Vanilla*
* **Remove All Non-Master Layers:** マスターレイヤーでもブレースレイヤーでもブラケットレイヤーでもないすべてのレイヤーを削除します。バックアップレイヤーを削除するのに便利です。Deletes all layers which are neither master layers, nor brace layers, nor bracket layers. Useful for getting rid of backup layers.
* **Reset Axis Mappings:** フォント内に現在存在するすべてのスタイル値に対して、 デフォルトの Axis Mappings パラ メーターを挿入 （またはリセット） し ます。マスターによって定義されたデザインスペースの範囲外のスタイル値を無視します。Inserts (or resets) a default Axis Mappings parameter for all style values currently present in the font. Ignores style values outside the designspace bounds defined by the masters. 
* **Short Segment Finder:** すべての補間を行い、ユーザーが指定したしきい値の長さよりも短いセグメントを見つけます。Goes through all interpolations and finds segments shorter than a user-specified threshold length. *要Vanilla*
* **Travel Tracker:** 点が必要以上に移動している補間を見つけます。結果は不完全で、通常は多くの誤検出がありますが、Shapeshifter スクリプトが見逃しているケースを発見することもあります。Finds interpolations in which points travel more than they should, i.e., can find wrongly hooked-up asterisks and slashes. The results are incomplete, and usually have many false positives, but it sometimes finds cases that the Shapeshifter script misses. *要Vanilla*
* **Variation Interpolator:** ユーザー定義の接尾辞を持つグリフのバリエーションをユーザー定義の数だけ作成します。同名のグリフを上書きする。Pablo Impallari の SimplePolator に似ています。デヴァナガリ・マトラの長さのバリエーションなどに有用。<https://www.youtube.com/watch?v=QDbaUlHifBc>.Creates a user-defined number of glyph variations with a user-defined suffix, containing interpolations between the layers and their respective backgrounds. Overwrites glyphs with same name. Similar to Pablo Impallari’s SimplePolator. Useful for e.g. length variants of Devanagari Matra, see José Nicolás Silva Schwarzenberg’s sample video: <https://www.youtube.com/watch?v=QDbaUlHifBc>. *要Vanilla*
* * **Other > Lines by Master:** 編集テキストをマスターにまたがって再複製し、編集ビューでマスターごとに1行ずつ追加します。注意してください、最初の改行以降はすべて無視されます。システム環境設定でキーボードを追加することを目的としています。Reduplicates your edit text across masters, will add one line per master in Edit view. Careful, ignores everything after the first newline. Intended for adding a keyboard in System Preferences.
* * **Other > Show Masters of Next/Previous Glyph:** 次から次へと一つのグリフを、すべてのマスターを使ってステップスルーできるようにします。次/前のグリフを表示する機能 (fn+左/右) と *Edit > Show All Masters* 機能を組み合わせたものです。システム環境設定でキーボードショートカットを付けるのに便利です。Allows you to step through one glyph after another, but with all masters. Combines the show next/previous glyph function (fn+left/right) with the *Edit > Show All Masters* function. Handy for attaching a keyboard shortcut in System Preferences.
* * **Other > Show Next/Previous Instance:** 現在の編集タブのプレビューセクションで、次の/前のインスタンスにジャンプします。システム環境設定でキーボードショートカットを付けるのに便利です。Jumps to next/previous instance in the preview section of the current Edit tab. Handy for attaching a keyboard shortcut in System Preferences.

## Kerning(カーニング)

*最も重要なのは、オートバンパー、カーネルクラッシャー、ギャップファインダー、サンプル文字列メーカーです。カーニングが多すぎる場合は、Exception Cleanerを検討してください。*
*Most important: Auto Bumper, KernCrasher, GapFinder, Sample String Maker. If you have too much kerning, consider Exception Cleaner.*

* **Adjust Kerning in Master:** すべてのカーニングペアに値を追加したり、すべてのペアに値を掛けたり、値で丸めたりするGUI。GUI to add a value to all kerning pairs, multiply all pairs by a value or round them by a value. *要Vanilla*
* **Auto Bumper:** 最小距離、左右のグリフを指定すると、Autokernは現在のマスターに必要最低限のカーニングを追加します。Specify a minimum distance, left and right glyphs, and Autokern will add the minimum necessary kerning for the current master. *要Vanilla*
* **Copy Kerning Exceptions to Double Accents:** `abreve`, `acircumflex`, `ecircumflex`, `ocircumflex`, `udieresis` のカーニング例外をベトナム語とピンインの二重アクセントにコピーします。Copies Kerning exceptions with abreve, `acircumflex`, `ecircumflex`, `ocircumflex`, `udieresis` into Vietnamese and Pinyin double accents.
* **Exception Cleaner:** すべての例外を、同じペアで利用可能なグループカーニングと比較します。差が閾値以下の場合は、カーニング例外を削除します。Compares every exception to the group kerning available for the same pair. If the difference is below a threshold, remove the kerning exception. *要Vanilla*
* **Find and Replace in Kerning Groups:** LとRのカーニンググループ内のテキストを検索したり、置換したりするためのGUI。検索フィールドは空白のままにしておきます。GUI for searching and replacing text in the L and R Kerning Groups, e.g. replace 'O' by 'O.alt'. Leave the search field blank for appending. *要Vanilla*
* **GapFinder:** 現在のフォントマスターに大きな隙間があるカーニングコンボの新しいタブを開きます。Opens a new tab with kerning combos that have large gaps in the current fontmaster. *要Vanilla*
* **Import Kerning from .fea File:** AFDKO コード内の kern 機能を含む .fea ファイルを選択すると、このスクリプトはカーニング値を最前面のフォントマスターにインポートしようとします (*Window > Kerning* を参照)。Choose an .fea file containing a kern feature in AFDKO code, and this script will attempt to import the kerning values into the frontmost font master (see *Window > Kerning*).
* **KernCrash Current Glyph:** カレントフォントマスターで衝突するカレントグリフとのカーニングコンボを含む新しいタブを開きます。Opens a new tab containing kerning combos with the current glyph that collide in the current fontmaster.
* **KernCrasher:** 現在のフォントマスターでクラッシュするカーニングコンボの新しいタブを開きます。Opens a new tab with Kerning Combos that crash in the current fontmaster. *要Vanilla*
* **New Tab with All Group Members:** 2 つのグリフ、例えば 'Ta' を選択してスクリプトを実行すると、右のカーニンググループ T と左のカーニンググループ a のすべての組み合わせを含む新しいタブが開きます。Select two glyphs, e.g. ‘Ta’, run the script, and it will open a new tab with all combinations of the right kerning group of T with the left kerning group of a.
* **New Tab with Glyphs of Same Kerning Groups:** カレントグリフの左右のカーニンググループのすべてのメンバを含む新規タブを開きます。Opens a new tab containing all members of the left and right kerning groups of the current glyph.
* **New Tab with Kerning Missing in Masters:** 各マスターの新しいタブを開き、このマスターではカーニングが存在しないが他のマスターでは存在することを表示します。Opens New Tabs for each master showing kerning missing in this master but present in other masters.
* **New Tab with Large Kerning Pairs:** 与えられたしきい値を超えたすべての正と負のカーニングペアをリストアップします。Lists all positive and negative kerning pairs beyond a given threshold. *要Vanilla*
* **New Tab with Overkerned Pairs:** しきい値のパーセンテージを尋ね、幅のしきい値を超えたすべての負のカーンペアを含む新しいタブを開きます。例。しきい値が 40% で、カンマの幅が 160 の場合、スクリプトは、カンマが 64 より大きい負の kern ペアをすべて報告します (160 の 40%)。r-カンマが-60であり、P-カンマが-70であると仮定します。この場合、後者を報告しますが、前者は報告しません。Asks a threshold percentage, and opens a new tab with all negative kern pairs going beyond the width threshold. Example: With a threshold of 40%, and a comma with width 160, the script will report any negative kern pair with comma larger than 64 (=40% of 160). Assume that r-comma is kerned -60, and P-comma is kerned -70. In this case, it would report the latter, but not the former. *要Vanilla*
* **New Tab with Right Groups:** 各右カーニンググループのグリフを1つずつ持つ新しいタブを作成します。右カーニンググループの整合性を調べるのに便利です。Creates a new tab with one glyph of each right group. Useful for checking the consistency of right kerning groups.
* **New Tab with all Selected Glyph Combinations:** 選択したグリフを取り込み、その文字のすべての組み合わせで新しいタブを開きます。また、タブのオープンに失敗した場合に備えて、マクロウィンドウにコピーするための文字列を出力します。Takes your selected glyphs and opens a new tab with all possible combinations of the letters. Also outputs a string for copying into the Macro window, in case the opening of the tab fails.
* **New Tab with Uneven Symmetric Kernings:** ATA AVA TOT WIWなどの対称文字のカーンペアを見つけ、ATがTAなどと同じかどうかを確認します。Finds kern pairs for symmetric letters like ATA AVA TOT WIW etc. and sees if AT is the same as TA, etc.
* **New Tabs with Punctuation Kern Strings:** 句読点付きのカーン文字列で複数のタブを出力します。Outputs several tabs with kern strings with punctuation.
* **Remove all Kerning Exceptions:** グループ間のカーニングを除いて、現在のマスターのすべてのカーニングを削除します。注意してください。Removes all kerning for the current master, except for group-to-group kerning. Be careful.
* **Remove Kerning Between Categories:** グリフ、カテゴリ、サブカテゴリ、スクリプト間のカーニングを削除します。Removes kerning between glyphs, categories, subcategories, scripts. *Requires Vanilla.*
* **Remove Kerning Pairs for Selected Glyphs:** 選択されたグリフを持つすべてのカーニングペアを、現在のマスターに対してのみ削除します。Deletes all kerning pairs with the selected glyphs, for the current master only.
* **Remove Orphaned Group Kerning:** フォント内にないグループを参照しているグループカーニングをすべて削除します。Deletes all group kernings referring to groups that are not in the font.
* **Remove Small Kerning Pairs:** 指定された値よりも小さい値、またはゼロに等しい値を持つ、現在のフォントマスタ内のすべてのカーニングペアを削除します。注意してください。Removes all kerning pairs in the current font master with a value smaller than specified, or a value equal to zero. Be careful. *要Vanilla*
* **Report Kerning Mistakes:** 不要なカーニングやグループ化を見つけようとします。レビューのためにマクロウィンドウでレポートします。Tries to find unnecessary kernings and groupings. Reports in Macro window, for reviewing.
* **Sample String Maker:** ユーザー定義のカテゴリに対するカーニング文字列を作成し、それをサンプル文字列に追加します。グループカーニングのみで、グループのないグリフは無視されます。Creates kern strings for user-defined categories and adds them to the Sample Strings. Group kerning only, glyphs without groups are ignored. *要Vanilla*
* **Set Kerning Groups:** 選択されているすべてのグリフに対して左右のカーニンググループを設定します。化合物の場合は基底成分のグループを使用しますが、そうでない場合は組み込み辞書に基づいて情報に基づいた推測を行います。Sets left and right kerning groups for all selected glyphs. In the case of compounds, will use the groups of the base components, otherwise makes an informed guess based on a built-in dictionary.
* **Steal Kerning from InDesign:** InDesignでセットされたテキストからカーニングを盗み出します。InDesignの[Optical Kerning](https://web.archive.org/web/20160414170915/http://blog.extensis.com/adobe/about-adobe's-optical-kerning.php)の値を抽出するのに便利です。Steals the kerning from text set in InDesign. Useful for extracting InDesign’s [Optical Kerning](https://web.archive.org/web/20160414170915/http://blog.extensis.com/adobe/about-adobe’s-optical-kerning.php) values.
* **Steal Kerning Groups from Font:** 選択されたすべてのグリフの左右のカーニンググループを 2 番目のフォントから盗み出します。Steals left/right kerning groups for all selected glyphs from a 2nd font. *要Vanilla*
* **Zero Kerner:** 1つのマスターでは欠落していても他のマスターでは存在するペアに対して、値ゼロのグループカーニングを追加します。OTVarエクスポートで補間可能なカーニングを保持するのに役立ちます。Add group kernings with value zero for pairs that are missing in one master but present in others. Helps preserve interpolatable kerning in OTVar exports. *要Vanilla*

## Paths(パス)

*アスタリスクにはRotate Around Anchorを使用しています。アウトラインチェックに重要。パス問題検出器、垂直方向のミスを検出、緑青マネージャ。Rewire Fireは、シェイプエッジ（アンチエイリアシングでダークスポットを作る）でのアウトラインセグメントの重複を減らすのに役立つので、OTVar制作で重要になっています。*
*I use Rotate Around Anchor for my asterisks. Important for outline checking: Path Problem Finder, Find Near Vertical Misses and the Green Blue Manager. Rewire Fire has become important in OTVar production, because it helps reduce duplicate outline segments at shape edges (which create dark spots in anti-aliasing).*

* **Align Selected Nodes with Background:** 選択されたノードを、以前に移動したノードに既に取られていない限り、最も近い背景ノードに整列させます。単一のノードを背景に整列させるための Cmd-Shift-A と同様ですが、複数のノードを整列させるためには、Cmd-Shift-A を使用します。Align selected nodes with the nearest background node unless it is already taken by a previously moved node. Like Cmd-Shift-A for aligning a single node with the background, but for multiple nodes.
* **Copy Glyphs from Other Font into Backup Layers:** ターゲットフォント内の選択されたグリフのためのバックアップレイヤーを作成し、それらをソースフォントからのそれぞれのグリフで塗りつぶします。あるフォントのグリフを別のフォントのブラケットレイヤーとして追加したい場合に便利です。Creates backup layers for selected glyphs in target font, and fills them with the respective glyphs from source font. Useful if you want to add glyphs from one font as bracket layers in another. *要Vanilla*
* **Distribute Nodes:** 水平または垂直にノードを分配します (選択枠の幅と高さの比に依存します)。Horizontally or vertically distributes nodes (depends on the width/height ratio of the selection bounding box).
* **Enlarge Single-Unit Segments:** 1単位より短い線分の長さを2倍にします。Doubles the length of line segments shorter than one unit.
* **Fill Up with Rectangles:** 選択したグリフを調べ、空のグリフを見つけたらプレースホルダ矩形を挿入します。テスト用のダミーフォントを素早く構築するのに便利です。Goes through your selected glyphs, and if it finds an empty one, inserts a placeholder rectangle. Useful for quickly building a dummy font for testing.
* **Find Near Vertical Misses:** 近いが、垂直方向のメトリクス上では正確ではないノードを見つけます。Finds nodes that are close but not exactly on vertical metrics. *要Vanilla*
* **Green Blue Manager:** ノードが青に設定され、下に緑に設定される角度を定義します。Define an angle above which a node will be set to blue, below which it will be set to green. *要Vanilla*
* **Grid Switcher:** フローティングボタンをクリックするだけで、グリッドを2つのグリッドステップ値の間で切り替えます。Toggles grid between two user-definable gridstep values with the click of a floating button. *要Vanilla*
* **Harmonise Curve to Line:** 2つのセグメント間の遷移が滑らかになるように（調和するように）、（選択された）曲線セグメント上のハンドルを、後続の線分と一緒に再配置します。Will rearrange handles on (selected) curve segments with a following line segment, in such a way that the transition between the two segments is smooth (harmonized).
* **New Tab with Small Paths:** ユーザー定義のしきい値サイズよりも小さいパスを四角い単位で含む新しいタブを開きます。Opens a new tab containing paths that are smaller than a user-definable threshold size in square units.
* **Path Problem Finder:** アウトラインのあらゆる種類の潜在的な問題を発見し、影響を受けたレイヤーで新しいタブを開きます。Finds all kinds of potential problems in outlines, and opens a new tab with affected layers. *要Vanilla*
* **Position Clicker:** クリックがうまくいかない位置図形の組み合わせをすべて見つけます。'クリックする'とは、重なり合ったときに2点座標を共有することを意味します。Finds all combinations of positional shapes that do not click well. ‘Clicking’ means sharing two point coordinates when overlapping. *要Vanilla*
* **Realign BCPs:** 選択されているすべてのグリフ内のすべての BCP を再調整します。ナッジやその他の変換の後や補間の後など、ハンドルが同期しなくなった場合に便利です。選択したグリフのすべてのレイヤーに適用するには Option を押したままにします。Realigns all BCPs in all selected glyphs. Useful if handles got out of sync, e.g. after nudging or some other transformation, or after interpolation. Hold down Option to apply to all layers of the selected glyph(s).
* **Remove all Open Paths:** 選択されているすべてのグリフの可視レイヤー内のすべての*開いている*パスを削除します。Deletes all *open* paths in the visible layers of all selected glyphs.
* **Remove Nodes and Try to Keep Shape:** 選択されたオンカーブノードを削除し、できるだけ形状を維持しようとします。1つのノードを削除したときに起こることと似ていますが、複数のノードを選択したときに起こります。プロのヒント: スクリプトを実行中に Shift キーを押したままにしておくと、残りのハンドルも可能な限りバランスをとってくれますが、これはまさに単一のノードを削除したときに起こることです。Deletes selected on-curve nodes and tries to keep the shape as much as possible. Similar to what happens when you delete a single node, but for a selection of multiple nodes. Pro tip: Hold down the Shift key while running the script, and it will also balance the remaining handles as much as possible, which is exactly what happens when you delete a single node.
* **Remove Short Segments:** 1 単位未満のセグメントを削除します。Deletes segments shorter than one unit.
* **Remove Stray Points:** 選択したグリフ内の迷点 (単一ノードパス) を削除します。注意：迷点は、自動整列を無効にするための手っ取り早い方法として使われることがあります。マクロウィンドウに詳細を報告します。Deletes stray points (single node paths) in selected glyphs. Careful: a stray point can be used as a quick hack to disable automatic alignment. Reports in detail to the Macro window.
* **Rewire Fire:** 重複した座標を見つけ、選択し、マークします。同じ位置にある2つのノードは、通常、再接続ノードを使用して再配線することができます。Finds, selects and marks duplicate coordinates. Two nodes on the same position typically can be rewired with Reconnect Nodes. *要Vanilla*
* **Rotate Around Anchor:** 'rotate'アンカーを中心にグリフやノードやコンポーネントの選択を回転させるためのGUI。ステップとリピートが可能。GUI for rotating glyphs or selections of nodes and components around a 'rotate' anchor. Allows to step and repeat. *要Vanilla*
* **Set Transform Origin:** 回転ツールの変形原点を数値で設定するためのシンプルなGUI。スケールツールにも効果があるはずです。Simple GUI for setting the Transform Origin of the Rotate tool numerically. Should also have an effect on the Scale tool. *要Vanilla*
* **Straight Stem Cruncher:** すべてのレイヤーの点間の距離を見つけ、それを(許容差を使って)指定されたステム幅と比較します。図面上でステムがずれているグリフをリストアップします。Finds distances between points in all layers, and compares them (with a tolerance) to specified stem widths. Lists glyphs that have deviating stems in their drawings. *要Vanilla*
* **Tunnify:** 少なくとも一つのハンドルが選択されているすべてのパスセグメントを探します。そして、セグメントのハンドルを均等にします。Adobe Illustrator のゼロハンドル (1つのハンドルが最も近いノードに引っ込んであるセグメント) を修正することができます。このスクリプトのアイデアは Eduardo Tunni (pablo Impallari さんが報告しています) から得たもので、それがスクリプトのタイトルになっています。しかし、私はEduardoのアルゴリズムを見たことがないので、私の実装は彼のものとは少し違うかもしれません。Looks for all path segments where at least one handle is selected. Then, evens out the handles of the segments, i.e., they will both have the same Fit Curve percentage. Can fix Adobe Illustrator's zero-handles (segments with one handle retracted into the nearest node). The idea for this script came from Eduardo Tunni (as colported by Pablo Impallari), hence the title of the script. I have never seen Eduardo's algorithm though, so my implementation might be a little different to his, especially the treatment of zero-handles.

## Pixelfonts(ピクセルフォント)

*これらのスクリプトは、ピクセルコンポーネントを粗いグリッドに配置する、pixelfontのワークフローに便利です。ピクセルデザインを行う場合は、ウィンドウ > プラグインマネージャで利用可能なピクセル関連のプラグインを参照してください。*
*These scripts are useful for a pixelfont workflow, where you place a pixel component in a coarser grid. If you are doing pixel designs, take a look at the pixel-related plug-ins available in Window > Plugin Manager.*

* **Align Anchors to Grid:** ダイアクリティックアンカーをフォントグリッドにスナップします。Snaps diacritic anchors onto the font grid.
* **Delete Components out of Bounds:** コンポーネントが通常の座標からはみ出して配置されている場合（グリッドステップの高いcmd-arrowコンポーネントを使用している場合に発生します）、このスクリプトはそれらを削除します。If a component is placed far outside the usual coordinates (happens when you cmd-arrow components with a high grid step), this script will delete them.
* **Delete Duplicate Components:** 重複したコンポーネント（名前と位置が同じ）を探して、1つだけを保持します。ピクセルフォントを展開しているときによく発生します。Looks for duplicate components (same name and position) and keeps only one. Happens frequently when buliding pixel fonts.
* **Flashify Pixels:** パスの自己交差を防ぐために小さな橋を作り、カウンターが白のままになるようにします。これは特に Flash フォントレンダラの問題であり、スクリプトの名前の由来となっています。Creates small bridges in order to prevent self-intersection of paths so counters stay white. This is especially a problem for the Flash font renderer, hence the name of the script.
* **Reset Rotated and Mirrored Components:** 拡大縮小、ミラーリング、回転されたコンポーネントを探し、それらをデフォルトのスケールと方向に戻しますが、その位置は維持されます。ミラーリングされたピクセルを修正するのに便利です。Looks for scaled, mirrored and rotated components and turns them back into their default scale and orientation, but keeps their position. Useful for fixing mirrored pixels.

## Smallcaps(スモールキャップ)

*フォントにSmallcapsを使用しているときは、常にCheck Smallcap Consistencyを実行しています。しかし、そのレポートには多くの誤検知が記載されており、すべての警告が同じように重要であるとは限りません。*
*When I have Smallcaps in my font, I always run Check Smallcap Consistency. Take its report with a grain of salt though: it lists a lot of false positives, and not every warning is equally important.*

* **Check Smallcap Consistency:** お使いの SC セットでいくつかのテストを実行し、マクロウィンドウ、特にカーニンググループとグリフセットにレポートします。Performs a few tests on your SC set and reports into the Macro window, especially kerning groups and glyph set.
* **Copy Kerning from Caps to Smallcaps:** キャップのカーニングペアを探し、それがフォント内で利用可能であれば、対応する.scグリフに対してそのカーニングを再複製します。注意してください。既存の SC カーニングペアを上書きします。Looks for cap kerning pairs and reduplicates their kerning for corresponding .sc glyphs, if they are available in the font. Please be careful: Will overwrite existing SC kerning pairs.

## Spacing(スペーシング)

*最も重要なこと。数学演算子の間隔の修正、メトリクス・マネージャーのブラケット化、矢印がある場合は矢印の位置の修正。新しいタブスクリプトは、図形を作成するときに便利です。*
*Most important: Fix Math Operator Spacing, Bracket Metrics Manager and, if you have arrows, Fix Arrow Positioning. The New Tab scripts are useful when creating figures.*

* **Bracket Metrics Manager:** ブラケット層のサイドベアリングと幅を管理します。Manage the sidebearings and widths of bracket layers, e.g., dollar and cent. *要Vanilla*
* **Center Glyphs:** 選択されたすべてのグリフを、 LSB=RSB となるように幅の内側にセンタリングします。Centers all selected glyphs inside their width, so that LSB=RSB.
* **Change Metrics by Percentage:** 選択したグリフのLSB/RSBをパーセント値で変更します。元に戻すボタンで元に戻す。Change LSB/RSB of selected glyphs by a percentage value. Undo with the Revert button. *要Vanilla*
* **Find and Replace in Metrics Keys:** LとRのメトリクス・キー内のテキストを検索して置換するためのGUI。検索フィールドは空白のままにして追加します。GUI for searching and replacing text in the L and R metrics keys, e.g. replace '=X+15' by '=X'. Leave the search field blank for appending.
* **Fix Arrow Positioning:** 指定されたデフォルトの矢印に依存する矢印の配置とメトリックキーを修正しました。メトリックキーを追加し、矢印を垂直方向に移動するようにした。新しいグリフは作成せず、既存のグリフでのみ動作するようにした。Fixes the placement and metrics keys of arrows, dependent on a specified default arrow. Adds metric keys and moves arrows vertically. Does not create new glyphs, only works on existing ones. *要Vanilla*
* **Fix Math Operator Spacing:** 幅と中心のグリフを +-×÷=≠±≈¬ のために同期させ、オプションでより小さい/より大きい記号やアスキー/アスキーチルデも同期させます。Syncs widths and centers glyphs for +−×÷=≠±≈¬, optionally also lesser/greater symbols and asciicircum/asciitilde. *要Vanilla* 
* **Freeze Placeholders:** 現在の編集タブでは、 現在のグリフに挿入されているすべてのプレースホルダを変更し、 そのプレースホルダを「フリーズ」させます。In the current Edit tab, will change all inserted placeholders for the current glyph, thus 'freeze' the placeholders.
* **Metrics Key Manager:** メトリックキーをカレントフォントに一括適用します。Batch apply metrics keys to the current font. *要Vanilla*
* **Monospace Checker:** 最前面のフォント内のすべてのグリフ幅が実際に等幅になっているかどうかをチェックします。マクロウィンドウで報告し、影響を受けるレイヤーのタブを開きます。Checks if all glyph widths in the frontmost font are actually monospaced. Reports in Macro Window and opens a tab with affected layers. *要Vanilla*
* **New Tab with all Figure Combinations:** 可能なすべての図形のコンボを含む新しいタブを開きます。また、タブのオープンに失敗した場合に備えて、マクロウィンドウにコピーするための文字列を出力します。Opens a new tab with all possible figure combos. Also outputs a string for copying into the Macro window, in case the opening of the tab fails.
* **New Tab with Fraction Figure Combinations:** 編集タブを開き、間隔とカーニングのための分数図形のコンボを表示します。Opens an Edit tab with fraction figure combos for spacing and kerning.
* **Remove Layer-Specific Metrics Keys:** 選択されているすべてのグリフのすべてのレイヤーにおいて、レイヤー (==) に固有の左右のメトリクスキーを削除します。また、グリフメトリクスキーを単純化する (すなわち、"=H" を "H" に変える)。Deletes left and right metrics keys specific to layers (==), in all layers of all selected glyphs. Also simplifies glyph metrics keys (i.e., turns "=H" into "H").
* **Remove Metrics Keys:** 選択されているすべてのグリフの左右のメトリクスキーを削除します。すべてのマスターとすべてのレイヤーに影響します。Deletes both left and right metrics keys in all selected glyphs. Affects all masters and all layers.
* **Reset Alternate Glyph Widths:** 接尾辞の付いたグリフの幅を、接尾辞の付いていないグリフの幅にリセットする。例えば、`Adieresis.ss01` は `Adieresis` の幅にリセットされる。Resets the width of suffixed glyphs to the width of their unsuffixed counterparts. E.g., `Adieresis.ss01` will be reset to the width of `Adieresis`.
* **Spacing Checker:** 変わったスペーシングを持つグリフを探して、新しいタブで開きます。Look for glyphs with unusual spacings and open them in a new tab. *要Vanilla*
* **Steal Metrics:** 選択されたすべてのグリフの横幅や横幅の値を、 2 番目のフォントから盗み取ります。オプションで、'=x+20' のようなメトリクスキーを転送することもできます。Steals the sidebearing or width values for all selected glyphs from a 2nd font. Optionally also transfers metrics keys like '=x+20'. *要Vanilla*
* **Tabular Checker:** 表形式のグリフを調べ、それが等幅かどうかを調べます。例外を報告します。Goes through tabular glyphs and checks if they are monospaced. Reports exceptions. *要Vanilla*

## Test(テスト)

*最も重要なのは、HTML スクリプトのテストです。AdobeやAppleのアプリでテキスト選択ハイライトが異常に高い、または低い場合は、Report Highest and Lowest Glyphsを実行して、その原因となっているグリフを見つけてください。言語レポートは標本を強化するためのものであり、権威ある情報を提供するものではありません。*
*Most important: the Test HTML scripts. If you have unusually high or low text selection highlights in Adobe or Apple apps, run Report Highest and Lowest Glyphs to find the glyph causing it. Language Report is just for beefing up your specimen, and will not give you authoritative information.*

* **Copy InDesign Test Text:** InDesignのテストテキストをクリップボードにコピーします。Copies a test text for InDesign into the clipboard.
* **Copy Word Test Text:** MS Wordのテストテキストをクリップボードにコピーします。Copies a test text for MS Word into the clipboard.
* **Language Report:** あなたのラテン文字でサポートされている言語の数と数についての予備的な情報を提供します。Underware の Latin-Plus リストをベースに、変更を加えています。Tries to give you a preliminary idea about how many and which languages are supported with your Latin characters. Based on Underware’s Latin-Plus list, with modifications.
* **Pangram Helper:** クリップボードにコピーしたり、新しいタブに入れたりすることができるパングラムを書くのに役立ちます。Helps you write a pangram, which you can copy into the clipboard, or put into a new tab. *要Vanilla*
* **Report Highest and Lowest Glyphs:** すべてのマスターについて、最高と最低の境界ボックスを持つグリフを報告します。Reports glyphs with highest and lowest bounding boxes for all masters.
* **Variable Font Test HTML:** 現在のVariation Font Exportフォルダ内に、現在のフォント用のテストHTMLを作成します。Create a Test HTML for the current font inside the current Variation Font Export folder.
* **Webfont Test HTML:** 現在のWebfont Exportフォルダ内のカレントフォントのテストHTMLを作成します。Creates a Test HTML for the current font inside the current Webfont Export folder, or for the current Glyphs Project in the project’s export path.

# ライセンス

Copyright 2011 The mekkablue Glyphs-Scripts Project Authors.

Some code samples by Georg Seifert (@schriftgestalt) and Tal Leming (@typesupply).

Some algorithm input by Christoph Schindler (@hop) and Maciej Ratajski (@maciejratajski).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use the software provided here except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

詳細は、このリポジトリに含まれるライセンスファイルを参照してください。
