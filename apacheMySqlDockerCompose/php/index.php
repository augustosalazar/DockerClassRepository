<?php

$link=@mysqli_connect("demo_db_1","root","my_secret_pw_shh","test_db");
if (!$link) {
    echo "Error: Unable to connect to MySQL." . PHP_EOL;
    echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
    exit;
}

$query = "SELECT * FROM latabla";

$result = mysqli_query($link,$query);

while ($row = mysqli_fetch_assoc($result))
{
    echo $row['name'], PHP_EOL;
}
mysqli_close($link);

?>
