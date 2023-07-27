import { Flex } from "@chakra-ui/react";
import React, { useState } from "react";
import Divider from "../components/Divider";
import Footer from "../components/Footer";
import Header from "../components/Header";
import Messages from "../components/Messages";

const Chat = () => {
    //device selected in first screen, used to append "For the 'deviceSelected', device..." to the beginning of each message
    const [deviceSelected, setDeviceSelected] = useState("");

    //list of messages in the current conversation
    const [messages, setMessages] = useState([
        { from: "assistant", text: "How can I help you today?" },
    ]);

    //list of messages in the initial selection screen
    const selectionMessages = [
        { from: "assistant", text: "Hello, which device can I help you with?" },
        { from: "select", text: "ePort G9" },
        { from: "select", text: "ePort G11" },
        { from: "select", text: "ePort Engage Combo" },
        { from: "select", text: "Ask about anything"}
    ];

    const [inputMessage, setInputMessage] = useState("");


    //appends loading message while response is being fetched
    const addLoading = () => {
        setMessages((old) => [...old, { from: "loading", text: "..." }]);
    }

    const removeLoading = () => {
        setMessages((old) => old.filter((msg) => msg.from !== "loading"));
    };

    //makes get request to backend api, appends message after retrieval
    const retrieveMessage = async (query) => {
        try {
            const response = await fetch(`http://127.0.0.1:5000/api/response?query="For the ${deviceSelected} device, ${query}"`);

            if (response.ok) {
                const data = await response.json();
                setMessages((old) => [...old, { from: "computer", text: data.response }]);
                removeLoading();
            }
        } catch (error) {
            console.error('Server error', error);
            removeLoading();
            setMessages((old) => [...old, { from: "computer", text: "Sorry, I'm having trouble answering your question. Please try again." }]);

        }
    };

    const handleSendMessage = async () => {
        if (!inputMessage.trim().length) {
            return;
        }
        const newMsg = inputMessage;

        setMessages((old) => [...old, { from: "me", text: newMsg }]);
        setInputMessage("");
        addLoading();
        try {
            retrieveMessage(newMsg);
        } catch (error) {
            console.error('Error retrieving message', error);
        }
  };

    return (
        <Flex w="100%" h="100vh" justify="center" align="center">
        <Flex w={["100%", "100%", "40%"]} h="90%" flexDir="column">
            <Header />
            <Divider />
            <Messages messages={deviceSelected === "" ? selectionMessages : messages} selected={deviceSelected} setSelected={setDeviceSelected}/>
            <Divider />
            {deviceSelected !== "" && (
                <Footer
                inputMessage={inputMessage}
                setInputMessage={setInputMessage}
                handleSendMessage={handleSendMessage}
                />
            )}
        </Flex>
        </Flex>
    );
};

export default Chat;
