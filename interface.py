class Interface():
    def get_title(self):
        print("請輸入圖書名稱：", end="")
        title = input().strip()
        return title;

    def get_init_file_str(self):
        print("請輸入起始文件編號：", end="")
        init_file_str = input().strip()
        return init_file_str;
    
    def get_max_file_str(self):
        print("請輸入最終文件編號：", end="")
        max_file_str = input().strip()
        return max_file_str;
        