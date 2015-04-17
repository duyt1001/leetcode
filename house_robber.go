package main

import "fmt"

func rob(num []int) int {
    var dp []int = make([]int, len(num)+1)
    if len(num) > 0 {
        dp[1] = num[0]
    }
    for i := 2; i <= len(num); i++ {
        //dp[i] = math.Max(dp[i-1], dp[i-2] + num[i-1])
        if dp[i-1] > dp[i-2] + num[i-1] {
            dp[i] = dp[i-1]
        } else {
            dp[i] = dp[i-2] + num[i-1]
        }
    }
    return dp[len(num)]
}

func main() {
    mainST := []int {12, 13, 12, 13, 12}
    fmt.Println(rob(mainST))
}
