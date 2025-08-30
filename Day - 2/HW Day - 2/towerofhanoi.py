def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    # Base case: no disks left to move
    if n == 0:
        return
    
    # Step 1: Move (n-1) disks from 'from_rod' → 'aux_rod' using 'to_rod' as helper
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    
    # Step 2: Move the largest disk (nth disk) from 'from_rod' → 'to_rod'
    print(f"Move disk {n} from {from_rod} to {to_rod}")
    
    # Step 3: Move (n-1) disks from 'aux_rod' → 'to_rod' using 'from_rod' as helper
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)

# Input from user
n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')
