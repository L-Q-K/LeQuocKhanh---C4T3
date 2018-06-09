from time import *

reason_pack = [
    {"B": "mới cắt tóc không nhận ra là phải",
     "C": "em ngu"},
    {"B": "7h15 rồi không muộn à",
     "C": "trả lời như cứt"},
    {"B": "dẹp trai như này mà kêu không ?",
     "C": "có hoặc không thế thôi"}
    ]

quiz_pack = [

    {
        "question": "Có nhận ra giảng viên không?",
        "choices": ["A. Có", "B. Không", "C. Anh là ai"],
        "right_choice": "A",
        "reason": reason_pack[0],
        "user_choice": ""
    },
    {
        "question": "Có đi muộn không?",
        "choices": ["A. Có", "B. Không","C. Ai bik =))"],
        "right_choice": "A",
        "reason": reason_pack[1],
        "user_choice": ""
    },
    {
        "question": "Trợ giảng có đẹp trai không?",
        "choices": ["A. Có", "B. Không","C. Tùy tâm"],
        "right_choice": "A",
        "reason": reason_pack[2],
        "user_choice": ""
    }
]

correct_answer_count = 0

for j in quiz_pack:
    print(j["question"])
    print()
    print(*j["choices"], sep="\n")
    print()

    user_choice = str(input("Your answer? ").upper())
    quiz_pack[quiz_pack.index(j)]["user_choice"] = user_choice
    if user_choice == j["right_choice"]:
        print("Bingo")
        quiz_pack[quiz_pack.index(j)]["point"] = True
        correct_answer_count += 1
    else:
        quiz_pack[quiz_pack.index(j)]["point"] = False
        print("Nah")

correct_answer_count  = format("%.2f" % (correct_answer_count / len(quiz_pack) * 100))

print("Your percentage: ", correct_answer_count, "%")


for i in range(len(quiz_pack)):
    if quiz_pack[i]["point"] == True:
        print("Câu", i + 1, "đúng")
    elif quiz_pack[i]["user_choice"] in list(quiz_pack[i]["reason"].keys()):
        print("Câu", i + 1, "sai vì", quiz_pack[i]["reason"][quiz_pack[i]["user_choice"]])
    else:
        print("Câu", i + 1, "sai vì không có dáp án này =((")

sleep(3)
