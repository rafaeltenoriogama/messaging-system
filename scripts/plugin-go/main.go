package main

import (
	"fmt"
	"log"

	"github.com/afajl/gojmx/jmx"
)

func main() {
	conn, err := jmx.NewClient("localhost", 9999)
	if err != nil {
		log.Fatalf("Failed to connect to JMX: %v", err)
	}
	defer conn.Close()

	// Exemplo de MBean do Kafka (ajuste conforme seu caso)
	attr, err := conn.GetAttribute("kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec", "Count")
	if err != nil {
		log.Fatalf("Failed to get attribute: %v", err)
	}

	fmt.Println(attr.Value)
}
