package main

import "fmt"


func CalcArea(r float32) float32 {
	var pi float32 = 3.14

	// var area float32 = (r * r) * pi
	var area float32
	area = (r * r) * pi
	
	fmt.Println("半径", r ,"の円の面積:", area)
	return area
}

func main() {
	var compareR float32 = 3 
	
	var baseArea float32 = 0
    var r float32 = 1    //r = 半径
	baseArea = CalcArea(r)

	var compareArea float32 = 0 
	compareArea = CalcArea(compareR)
	fmt.Println(compareArea / baseArea)
}
