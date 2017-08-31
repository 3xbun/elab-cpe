midterm = float(input())
if midterm >= 0:
    if midterm <= 60:
        final = float(input())
        if final >= 0:
            if final <= 60:
                total = midterm + final
                avg = total/2
                print('Total: ' + str(total))
                print('Average: ' + str(avg))
