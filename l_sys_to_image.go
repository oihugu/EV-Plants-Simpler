package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	type command_pattern struct {
		command string `json:"command"`
	}

	var str = `{"command" : "stack_append"}`

	// Open our jsonFile
	// jsonFile, err := os.Open("./temp_json/temp_copy.json")

	// // if we os.Open returns an error then handle it
	// if err != nil {
	// 	fmt.Println(err)
	// }

	//byteValue, _ := ioutil.ReadAll(jsonFile)

	//var commands command_pattern

	var m command_pattern

	if err := json.Unmarshal([]byte(str), &m); err != nil {
		panic(err)
	}

	fmt.Printf("%+v\n", m)

	//defer jsonFile.Close()

}
