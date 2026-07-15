class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud = deque(students)
        for s in sandwiches:
            num_stud = len(stud)
            while num_stud != 0:
                if stud[0] == s:
                    stud.popleft()
                    break
                else:
                    stud.append(stud.popleft())
                    num_stud -= 1
            else:
                # inner while completed without breaking → no one wants this sandwich
                return len(stud)
        return len(stud)