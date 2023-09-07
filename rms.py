import rumps

class App(rumps.App):
    def __init__(self):
        super(App, self).__init__("App")
        # メニューリストを登録
        self.menu = ["Parent"]
        # メニューは入れ子にできる
        self.menu["Parent"].add("Child1")
        self.menu["Parent"].add("Child2")
        self.menu["Parent"]["Child2"].add("GrandChild1")
        self.menu["Parent"]["Child2"].add("GrandChild2")
        # メニューバーアイコンも設定可能
        # self.icon = "icon.png"

    # rumps.clickedデコレータでもメニューを追加できる
    # rumps.clicked()の第一引数はメニューラベルになる
    # デコレートされた関数/メソッドは引数senderをとる
    @rumps.clicked("Alert!")
    def alert(self, _):
        # アラートダイアログ
        rumps.alert("Hello!")

    @rumps.clicked("Notify!")
    def notification(self, _):
        # Macの通知
        rumps.notification(message="Hello World!",
                           title="Hello!",
                           subtitle="World!")

    @rumps.clicked("Off")
    def switch(self, sender):
        # メニューにチェックマークをつける
        sender.state = not sender.state
        sender.title = "On" if sender.state else "Off"

    @rumps.clicked("Show Window!")
    def window(self, _):
        # テキストエディットを含むウィンドウを表示
        rumps.Window(message="Showing Window!",
                     title="Window",
                     default_text="default text...",
                     ok="Submit!",
                     cancel="Cancel...").run()

    @rumps.clicked("Start Timer!")
    def timer(self, _):
        # 一定時間ごとに処理を実行するタイマー

        count = 0

        # callback関数は引数にTimerオブジェクトをとる
        def counter(t):
            nonlocal count
            count += 1
            print(count)
            if count >= 10:
                print("Stop Timer!")
                t.stop()

        # タイマーオブジェクト
        # 一定時間ごとにcallbackを呼び出す
        timer = rumps.Timer(callback=counter, interval=1)
        timer.start()


    # クラスメンバでなくとも、clickedデコレータを関数に付加するとメニューは追加される
    @rumps.clicked("outer")
    def outer(_):
        pass


if __name__ == "__main__":
    App().run()