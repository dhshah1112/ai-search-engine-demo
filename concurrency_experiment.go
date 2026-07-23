package main

import (
	"fmt"
	"sync"
	"time"
)

// Compares wall-clock time for two indexing tasks run
// sequentially vs. concurrently with goroutines.
func processSearch(item string, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 0; i < 5; i++ {
		fmt.Println("Indexing:", item, i)
		time.Sleep(time.Millisecond * 500) // stands in for I/O wait
	}
}

func main() {
	start := time.Now()
	var wg sync.WaitGroup
	wg.Add(2)
	go processSearch("Vector_DB_Updates", &wg)
	go processSearch("Keyword_Index_Updates", &wg)
	wg.Wait() // without this, main can exit before the goroutines finish
	fmt.Printf("Concurrent elapsed: %v (sequential would be ~5s)\n", time.Since(start))
}
