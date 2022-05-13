def towers(disks, source, extra, destin):
    if disks == 1:
        print("Moved disk from " + source + " to " + destin)
        return 1
    else:
        count = 0
        count += towers(disks - 1, source, destin, extra)
        count += towers(1, source, extra, destin)
        count += towers(disks - 1, extra, source, destin)
        return count


numdisks = int(input("Enter the number of disks."))

src = "A"
xtra = "B"
destination = "C"
numcalls = towers(numdisks, src, xtra, destination)
print("Number of calls to towers = " + str(numcalls))
