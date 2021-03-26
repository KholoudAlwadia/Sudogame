
# part 2
board = [
    [3, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 0],
    [2, 0, 0, 0, 3, 0, 8, 0, 5],
    [0, 8, 1, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 6, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 4, 0],
    [5, 0, 4, 0, 1, 0, 0, 0, 3],
    [0, 6, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 4]
]

#Part 1

def print_board(bo): # اعدادات طباعة البورد
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
def solve(bo):
    find = find_empty(bo) #يسند قيمة الخانة الفارغة للقيمة
    if not find: # يتحقق من ان الخانه ليست فارغة من خلال القيمة المسند اليها مسبقاُ
        return True # يرجع صح
    else: # او يجعل البوزيشين المتكون من الثف و العامود فارغ
        row, col = find

    for i in range(1,10):    #لكل خانة في البورد
        if valid(bo, i, (row, col)):   # اذا ان القيمة موجودة فسيقوم باسناد قيمة لكل بوزيشن
            bo[row][col] = i
            if solve(bo): # و يستدعي دالة التحقق اذا الخانة فارغة ليكمل الحل او ليرجع القيمة خطأ و يرجع البوزيشن 0 و يتيح له من خلال اللوب بان يجرب قيم اخرى
                return True
            bo[row][col] = 0
    return False

def valid(bo, num, pos):   # Function to check if the choice is correct

    # Check row
    for i in range(len(bo[0])): #loop through every single column in the row
        if bo[pos[0]][i] == num and pos[1] != i: #pos[0] != i means we don't check the position we insert in
            return False

    # Check column
    for i in range(len(bo)): #loop through every single row in the column
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    # the two next line to determine which box we will check
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # next line loop through the 9 elements of the box
    for i in range(box_y*3, box_y*3 + 3): # we multiply by 3 to get the index of the elements
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos: #(i,j) != pos means we don't check the position we insert in
                return False

    # we sure every thing is okay so the number is valid to insert
    return True


def find_empty(bo): # لإرجاع الخانات التي تحتوي على صفر ك بوزيشن ، و اذا ما لقى فا عادي ينهيها
    for i in range(len(bo)):
        for j in range(len(bo[0])):
             if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
