import React from "react";
import { Flex, Input, Button } from "@chakra-ui/react";

//query/chat bar component
const Footer = ({ inputMessage, setInputMessage, handleSendMessage }) => {

  return (
    <Flex w="100%" mt="5">
      <Input
        placeholder="Type Something..."
        border="none"
        borderRadius="none"
        _focus={{
            boxShadow: "none", 
            border: "none",
        }}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSendMessage();
          }
        }}
        value={inputMessage}
        onChange={(e) => setInputMessage(e.target.value)}
      />
      <Button
        bg="#fb8333"
        color="white"
        borderRadius="md"
        _hover={{
          bg: "white",
          color: "black",
          border: "1px solid black",
        }}
        disabled={inputMessage.trim().length <= 0}
        onClick={handleSendMessage}
        
      >
        Send
      </Button>
    </Flex>
  );
};

export default Footer;
