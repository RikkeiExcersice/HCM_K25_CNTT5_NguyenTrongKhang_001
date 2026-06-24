class Player:
    def __init__(self, id, name, speed_score, technique_score, goal_score, average_score, performance_type):
        self.id = id
        self.name = name
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goal_score = goal_score
        self.average_score = average_score
        self.performance_type = performance_type

    def calculate_average():
        return speed_score * 30/100 + technique_score * 40/100 + goal_score * 30/100

    def classify_performance(self):
        if average_score < 0 or average_score > 10.0:
            raise ValueError
        
        if average_score < 5.0:
            performance_type = "Dự bị yếu"
        elif average_score < 6.5:
            performance_type = "Trung bình"
        elif average_score < 8.0:
            performance_type = "Tốt"
        else:
            performance_type = "Ngôi sao"

        return performance_type

class PlayerManager():
    def __init__(self):
        self.players = []

    def add_player(self):
        id = input("Mời bạn nhập id: ")
        name = input("Mời bạn nhập tên: ")
        speed_score = input("Mời bạn nhập điểm tốc độ: ")
        technique_score = input("Mời bạn nhập điểm kỹ thuật: ")
        goal_score = input("Điểm ghi bàn: ")
        average_score = Player.calculate_average
        performance_type = Player.classify_performance
        player = Player(id, name, speed_score, technique_score, goal_score, average_score, performance_type )
        self.players.append(player)
        print("Thêm cầu thủ thành công !!!")
        

    def show_all(self):
        print(f"{'Mã cầu thủ':<15} | {'Họ tên':<20} | {'Tốc độ':<15} | {'Kỹ thuật':<15} | {'Ghi bàn':<15} | {'Điểm phong độ':<15} | {'Phân loại':<30} ")
        for player in self.players:
            print(f"{player.id:<15} | {player.name:<20} | {player.speed_score:<15} | {player.technique_score:<15} | {player.goal_score:<15} | {player.average_score:<15} | {player.performance_type:<30}")
            print("-" * 115)


    def update_player(self):
        update_id = input("Mời bạn nhập id cầu thủ cần cập nhật: ")
        for player in self.players:
            if player[id] == update_id:
                new_speed_score = input("Mời bạn nhập chỉ số tốc độ mới: ")
                new_technique_score = input("Mời bạn nhập chỉ số kĩ thuật mới: ")
                new_goal_score = input("Mời bạn nhập chỉ số ghi bàn mới: ")

                player[speed_score] = new_speed_score
                player[technique_score] = new_technique_score
                player[goal_score] = new_goal_score
            
        else:
            print("Không tìm thấy cầu thủ có id: ", update_id)
            return
        
    def delete_player(self):
        del_id = input("Mời bạn nhập id cầu thủ cần xóa: ")
        for player in self.players:
            if player[id] == del_id:
                choice_del = input("Bạn có chắc muốn xóa cầu thủ này không? (Y/N)")
                if choice_del == 'Y':
                    self.players.remove(player)
                else:
                    print("Đã hủy xóa !")
                    return
        else: 
            print("Không có cầu thủ cần tìm")
            return
                
            

        

def main():
    while True:
        print("=============Menu=============")
        print("1. Hiển thị danh sách cầu thủ")
        print("2. Thêm cầu thủ mới")
        print("3. Cập nhật thông tin cầu thủ")
        print("4. Xóa cầu thủ")
        print("5. Tìm kiếm cầu thủ ")
        print("6. Thoát")
        print("=================================")
        choice = input("Mời bạn nhập lựa chọn: ")
        match choice:
            case '1':
                PlayerManager().show_all()
            case '2':
                PlayerManager().add_player()
            case '3':
                PlayerManager().update_player()
            case '4':
                PlayerManager().delete_player
            case '5':
                pass
            case '6':
                print("Đã thoát chương trình !!!")
                break
            case _:
                print("Vui lòng nhập lại !")


main()