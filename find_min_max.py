def find_min_max(arr):
    """
    Рекурсивно знаходить мінімальний та максимальний елементи масиву.

    Parameters:
        arr (list): Масив чисел.

    Returns:
        tuple: (мінімум, максимум)
    """
    def helper(left, right):
        # Базовий випадок: один елемент
        if left == right:
            return arr[left], arr[left]
        
        # Базовий випадок: два елементи
        if right == left + 1:
            if arr[left] < arr[right]:
                return arr[left], arr[right]
            else:
                return arr[right], arr[left]
        
        # Рекурсивний випадок
        mid = (left + right) // 2
        min1, max1 = helper(left, mid)
        min2, max2 = helper(mid + 1, right)

        return min(min1, min2), max(max1, max2)

    if not arr:
        raise ValueError("Масив не повинен бути порожнім")

    return helper(0, len(arr) - 1)

if __name__ == "__main__":
    # Приклад використання
    arr = [7, 2, 9, 4, -1, 6, 0]
    min_val, max_val = find_min_max(arr)
    print(f"Мінімум: {min_val}, Максимум: {max_val}")