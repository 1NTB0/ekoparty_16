<?php
$SOCK_DCCP                = 6;
$IPPROTO_DCCP             = 33;

$bind_address = "7e0a98bb084ec0937553472e7aafcf68ff96baf4.ctf.site";
$port = 20000;

$client_socket_fd = socket_create(AF_INET, $SOCK_DCCP, $IPPROTO_DCCP);

// $message = "asdfasdfasdfasdffwoeifjiowjefiojwieofjwoefji";

if (socket_connect ($client_socket_fd, $bind_address, $port)) {
//	        socket_send($client_socket_fd, $message, strlen($message), 0);
}

$recv = socket_read($client_socket_fd, 100);
echo $recv;

socket_close($client_socket_fd);

?>
