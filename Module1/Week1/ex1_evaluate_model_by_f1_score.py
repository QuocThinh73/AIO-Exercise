def cal_f1_score(tp, fp, fn):
    # Kiểm tra kiểu dữ liệu
    if type(tp) != int:
        print("tp must be int")
        return
    if type(fp) != int:
        print("fp must be int")
        return
    if type(fn) != int:
        print("fn must be int")
        return
    
    # Kiểm tra giá trị hợp lệ
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1_score is {f1_score}")


cal_f1_score(tp=2, fp=3, fn=4)
cal_f1_score(tp='a', fp=3, fn=4)
cal_f1_score(tp=2, fp='a', fn=4)
cal_f1_score(tp=2, fp=3, fn='a')
cal_f1_score(tp=2, fp=3, fn=0)
cal_f1_score(tp=2.1, fp=3, fn=0)           
