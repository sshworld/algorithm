def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1) :
        if phone_book[i][:len(phone_book[i])] == phone_book[i+1][:len(phone_book[i])] :
            return False
    return True

# def solution(phone_book):
#     phone_book.sort()
    
    
#     for p1, p2 in zip(phone_book, phone_book[1:]) :
#         print(p1, p2)
#         if p2.startswith(p1) :
#             return False
    
#     return True


    # hash_map = {}
    # for phone_number in phone_book:
    #     hash_map[phone_number] = 1
    # for phone_number in phone_book:
    #     temp = ""
    #     for number in phone_number:
    #         temp += number
    #         if temp in hash_map and temp != phone_number:
    #             return False
    # return True