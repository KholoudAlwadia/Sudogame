# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def print_board(bo):
        for i in range(len(bo)): # for whole board *عاموديا*
            if i % 3 == 0 and i != 0: # اذا وصل لثلاث خانات افقياً و ما كان عند اول خانة فا يطبع الفاصل الافقي بين المجموعات
                print("- - - - - - - - - - - - - ") #each 3 rows indivaduale


            for j in range(len(bo[0])): # يتحقق لكل خانة بالبورد لكل صف
                if j % 3 == 0 and j != 0: # اذا وصل للخانة الثالثة، حيث ان موقعه صار 3 ، و انه ليس على الخانة الاولى بموقع 0
                    print(" | ", end="") #  ابطع فاصل، بين كل 3 خانات

                if j == 8: # يتحقق لعدد خانات العامود ، اذا وصلت 8 *خانات المطلوب*
                    print(bo[i][j]) # يطبع البورد لانهاءها ب ابعادها
                else:  # يطبع اخر جزء من الاعداد حسب طول البورد و يطبع نهاية السطر بدون الانتقال لجديد
                    print(str(bo[i][j]) + " ", end="")


    def find_empty(bo): # لإرجاع الخانات التي تحتوي على صفر ك بوزيشن ، و اذا ما لقى فا عادي ينهيها
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)  # row, col

        return None



