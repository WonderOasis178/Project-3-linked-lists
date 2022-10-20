"""SList CLass for Project 3"""


class SList:
    class SListNode:
        def __init__(self, course=None):
            '''Initialize node object'''
            self.value = course
            self.course = course
            self.next = None

    def __init__(self):
        self._head = None
        self._size = 0
        self.first = None

    def insert(self, course):
        '''Function to insert a given node at its correct sorted position
          into a given list, sorted in increasing order'''
        n = self.SListNode(course)
        course_num = course.number()
        self._size += 1
        inserted = False
        # insert into an ascending oreder
        if self._head is None:  # empty list
            n.next = self._head
            self._head = n
        else:
            ptr = self._head
            while (ptr.next is not None):
                if ptr.course.number() <= course_num and ptr.next.course.number() >= course_num:
                    n.next = ptr.next
                    ptr.next = n
                    inserted = True
                    return
                ptr = ptr.next
            if not inserted:
                ptr.next = n

    def find(self, value):
        '''Search for a value in the list, return it if found, None otherwise'''
        # initialize current to head
        current = self._head
        # loop till current not equal to None
        while current is not None:
            if current.value == value:
                return value  # data found
            current = current.next
        return None  # Data Not found

    def size(self):
        """Returns total number of courses in the linked list"""
        temp = self._head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def remove(self, value):
        '''Remove the first occurance of value.'''
        '''temp = self._head
        if temp and temp.value == value:
            self._head = temp.next
            temp = None
            return
        while temp:
            if temp.value == value:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None'''
        ptr = self.head
        prev_ptr = None
        while ptr is not None:
            if ptr.course.number() == value:

                if prev_ptr is None:
                    self.head = ptr.next
                else:
                    prev_ptr.next = ptr.next

                del ptr
                self._size -= 1
                return 1

            prev_ptr = ptr
            ptr = ptr.next

        return 0

    def remove_all(self, key):
        '''Remove all instances of value'''
        temp = self._head
        # if head is not null and value stored at head == to key,
        # keep adjusting head as head.next & deleting previous head
        # until new head becomes null or != to key
        while temp is not None and temp.value == key:
            node_to_delete = temp
            temp = temp.next
            node_to_delete = None
        # Delete occurrences other than head list and delete nodes
        # with value equal to key, and adjust links accordingly
        if temp is not None:
            while temp.next is not None:
                if temp.next.value == key:
                    node_to_delete = temp.next
                    temp.next = temp.next.next
                    node_to_delete = None
                else:
                    temp = temp.next

    def __str__(self):
        """Convert the list to a string and return it"""
        current = self._head
        if current is None:
            return None
        out = '[ ' + str(current.value) + ' \n'
        while current.next is not None:
            current = current.next
            out += str(current.value) + ' \n'
        return out + ']'

    def __iter__(self):
        '''Return an iterator for the list'''
        current = self._head
        while current is not None:
            yield current
            current = current.next

    def __getitem__(self, index):
        '''Return the item at the given index, or throw an exception if invalid index'''
        current = self._head
        count = 0
        # Loop while end of linked list is not reached
        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next
        # asking for a nonexistent num
        raise ValueError("Index does not exist")

    def __len__(self):
        '''Return the lenght of the linked list'''
        return self._size
