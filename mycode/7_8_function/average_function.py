# list에 저장된 값의 평균을 계산하는 함수 정의
def my_average(numbers):
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers)
    return int(avg)

def main():
    my_list = [20,50, 60, 100, 30]
    result = my_average(my_list)
    print(f"평균값은 {result}")

main()

