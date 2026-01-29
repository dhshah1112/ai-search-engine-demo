package main

import (
	"fmt"
	"time"
)

// This experiment tests if Go routines handle parallel tasks 
// better than Python threads for our search indexer.
func processSearch(item string) {
	for i := 0; i < 5; i++ {
		fmt.Println("Indexing:", item, i)
		time.Sleep(time.Millisecond * 500)
	}
}

func main() {
	// The 'go' keyword spins this off into a lightweight thread
	go processSearch("Vector_DB_Updates")
	processSearch("Keyword_Index_Updates")
}