import React, { useEffect, useRef, useState } from "react";
import { Avatar, AvatarBadge, Flex, Text, CSSReset, ChakraProvider } from "@chakra-ui/react";
import ctlpLogo from '../assets/small-logo.png';
import { motion } from "framer-motion";

//component for middle section, contains messages
const Messages = ({ messages, selected, setSelected}) => {
  const AlwaysScrollToBottom = () => {
    const elementRef = useRef();
    useEffect(() => elementRef.current.scrollIntoView());
    return <div ref={elementRef} />;
  };

  const [isHovered, setIsHovered] = useState(false);

  const handleHover = () => {
    setIsHovered(true);
  };

  const handleHoverLeave = () => {
    setIsHovered(false);
  };

  const dotVariants = {
    hidden: {
      opacity: 0,
    },
    visible: {
      opacity: 1,
    },
  };
  
  return (
    <ChakraProvider>
      <CSSReset />
      {/*Flex wraps the entire component */}
      <Flex
        w="100%"
        h="80%"
        overflowY="auto" 
        flexDirection="column"
        p="3"
        sx={{
          '&::-webkit-scrollbar': {
            width: '0.4em',
            background: 'transparent'
          },
          '&::-webkit-scrollbar-thumb': {
            background: 'gray.200', 
            borderRadius: 'full',
          },
        }}
      >
        {/*
          Display all the messages contained in the state prop passed in
          4 types
          - me: messages sent by user, render on the right side
          - assistant: messages returned by chatbot, render on the left side
          - select: device selection messages, clickable and orange
          - loading: loading message, consists of three animated dots
        */}
        {messages.map((item, index) => {
          if (item.from === "me") {
            return (
              <motion.div
                key={index}
                positionTransition
                initial={{ opacity: 0, y: 100 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, transition: { duration: 0.15 } }}
              >
                <Flex w="100%" justify="flex-end">
                  <Flex
                    bg="#1d95db"
                    color="white"
                    minW="100px"
                    maxW="350px"
                    my="1"
                    p="3"
                    borderRadius="md"
                  >
                    <Text>{item.text}</Text>
                  </Flex>
                </Flex>
              </motion.div>
            );
          } else if (item.from === "select") {
            return (
              <motion.div
                key={index}
                positionTransition
                initial={{ opacity: 0, y: 100 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, transition: { duration: 0.15 } }}
              >
                <Flex
                  w="100%"
                  onClick={() => {
                    if (item.text === "Ask about anything") {
                      setSelected(" "); // Set deviceSelected to an empty string
                    } else {
                      setSelected(item.text); // Set deviceSelected to the item's text(device)
                    }
                  }}
                  onMouseEnter={handleHover}
                  onMouseLeave={handleHoverLeave}
                  alignItems="center"
                  _hover={{ cursor: "pointer" }}
                >
                  <Avatar
                    bg="white"
                    size="md"
                    marginRight="2"
                  />
                  <Flex
                    as={motion.div}
                    bg="#fb8333"
                    color="white"
                    minW="100px"
                    maxW="350px"
                    my="1"
                    p="3"
                    borderRadius="md"
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    boxShadow={isHovered ? "0 0 0 3px rgba(0, 0, 0, 0.1)" : "none"}
                  >
                    <Text>{item.text}</Text>
                  </Flex>
                </Flex>
              </motion.div>
            );
          } else if (item.from === "loading" ){
            return (
              <motion.div
                key={index}
                positionTransition
                initial={{ opacity: 0, y: 100 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, transition: { duration: 0.15 } }}
              >
                <Flex
                  w="100%"
                  alignItems="center"
                >
                  <Avatar
                    bg="white"
                    size="md"
                    marginRight="2"
                  />
                  <Flex
                    bg="gray.100"
                    color="black"
                    minW="100px"
                    maxW="350px"
                    my="1"
                    p="3"
                    borderRadius="md"
                  > 
                    <motion.span
                    variants={dotVariants}
                    initial="hidden"
                    animate="visible"
                    transition={{ duration: 0.5, repeat: Infinity }}
                    style={{ display: "inline-block", margin: "0.2rem" }}
                  >
                    {item.text.charAt(0)}
                  </motion.span>
                  <motion.span
                    variants={dotVariants}
                    initial="hidden"
                    animate="visible"
                    transition={{ duration: 0.5, delay: 0.2, repeat: Infinity }}
                    style={{ display: "inline-block", margin: "0.2rem" }}
                  >
                    {item.text.charAt(1)}
                  </motion.span>
                  <motion.span
                    variants={dotVariants}
                    initial="hidden"
                    animate="visible"
                    transition={{ duration: 0.5, delay: 0.4, repeat: Infinity }}
                    style={{ display: "inline-block", margin: "0.2rem" }}
                  >
                    {item.text.charAt(2)}
                  </motion.span>
                    
                  </Flex>
                </Flex>
              </motion.div>
            )
          } else {
            return (
              <motion.div
                key={index}
                positionTransition
                initial={{ opacity: 0, y: 100 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, transition: { duration: 0.15 } }}
              >
                <Flex w="100%">
                  <Avatar
                    src={ctlpLogo}
                    size="md"
                    marginRight="2"
                  >
                    <AvatarBadge boxSize="0.9em" bg="#5fd93d" />
                  </Avatar>
                  
                  <Flex
                    bg="gray.100"
                    color="black"
                    minW="100px"
                    maxW="350px"
                    my="1"
                    p="3"
                    borderRadius="md"
                  >
                    <Text>{item.text}</Text>
                  </Flex>
                </Flex>
              </motion.div>
            );
          }
        })}
        <AlwaysScrollToBottom />
      </Flex>
    </ChakraProvider>
  );
};

export default Messages;