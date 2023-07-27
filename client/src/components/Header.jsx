import React from "react";
import {Flex, Avatar, Text} from "@chakra-ui/react";
import ctlpLogo from "../assets/small-logo.png"

//component for orange bar at top with cantaloupe logo
const Header = () => {
    return (
        <Flex w="100%" bg="#fb8333">
            <Avatar size = "lg" name="cantaloupe" src={ctlpLogo} borderRadius="full" padding="2">
            </Avatar>
            <Flex flexDirection="column" mx="1" justify="center">
                <Text fontSize="lg" fontWeight="bold" color="white">
                Cantaloupe
                </Text>
            </Flex>
        </Flex>
    );
}

export default Header;