// https://leetcode.com/problems/unique-paths-iii/description/
// Accepted

func uniquePathsIII(grid [][]int) int {
	ystart, xstart := -1, -1
	moves := 0
	for y, row := range grid {
		for x, cell := range row {
			if cell == 1 {
				ystart, xstart = y, x
			} else if cell == 0 {
				moves = moves + 1
			}
		}
	}
	return enumerate("", grid, moves, ystart, xstart)
}

func enumerate(path string, grid [][]int, moves int, y int, x int) int {
	result := 0
	if y > 0 {
		result = result + try(path+"N", grid, moves, y, x, y-1, x)
	}
	if y < len(grid)-1 {
		result = result + try(path+"S", grid, moves, y, x, y+1, x)
	}
	if x > 0 {
		result = result + try(path+"W", grid, moves, y, x, y, x-1)
	}
	if x < len(grid[y])-1 {
		result = result + try(path+"E", grid, moves, y, x, y, x+1)
	}
	return result
}

func try(path string, grid [][]int, moves int, yold int, xold int, ynew int, xnew int) int {
	cell := grid[ynew][xnew]
	// fmt.Printf("%s moves=%d cell=%d (%d,%d)->(%d,%d)\n", path, moves, cell, yold,xold,ynew,xnew)
	if moves > 0 && cell == 0 {
		// moves left and empty square
		grid[yold][xold] = -2 // already been there
		result := enumerate(path, grid, moves-1, ynew, xnew)
		grid[yold][xold] = 0
		return result
	} else if moves == 0 && cell == 2 {
		// ending square and last move
		return 1
	}
	return 0
}