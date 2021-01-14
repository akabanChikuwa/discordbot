
class Schedule:
    #時間を設定するフォーマット
    time_format = '%Y/%m/%d/%H/%M'
    #スケジュールのディクショナリー
    schedule_list = {time_format:' '}
    #スケジュールを通知するチャンネルのid
    s_id =


    #スケジュールの追加
    def add(self,data,message):
        Schedule.schedule_list[data] = message
        print(Schedule.schedule_list[data])
    #スケジュールのリストを取得
    def get_list(self):
        return Schedule.schedule_list
    #データの削除
    def delete_date(self,key):
        Schedule.schedule_list.pop(key)
    #チャンネルidのセット
    def set_channel_id(self,id):
        self.s_id = id
    #チャンネルidの取得
    def get_channnel_id(self):
        return self.s_id


