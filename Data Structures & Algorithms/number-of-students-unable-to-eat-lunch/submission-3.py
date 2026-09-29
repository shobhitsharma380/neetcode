class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        sandwiches_queue = deque(sandwiches)
        counter = 0

        while students_queue and counter < len(students_queue):
            if students_queue[0] == sandwiches_queue[0]:
                students_queue.popleft()
                sandwiches_queue.popleft()
                counter = 0
            else:
                students_queue.append(students_queue[0])
                students_queue.popleft()
                counter +=1
                
        return len(students_queue)
