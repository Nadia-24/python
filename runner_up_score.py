n = int(input())
arr = map(int, input().split())

def runner_up(array):
    array = list(array)
    array.sort(reverse=True)
    print(array)
    for score in range(len(array)):
        if array[score] != array[score+1]:
            runner_up = array[score+1]
            break
        else:
            continue
    print(runner_up)

runner_up(arr)

    



    