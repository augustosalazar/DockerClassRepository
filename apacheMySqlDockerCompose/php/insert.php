<?php

if (isset($_GET['nombre'])) {

$link=@mysqli_connect("demo_db_1","root","my_secret_pw_shh","test_db");
if (!$link) {
    echo "Error: Unable to connect to MySQL." . PHP_EOL;
    echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
    exit;
}

$query = "SELECT * FROM latabla";
$elnombre = $_GET['nombre'];
$queryInsert ="INSERT INTO latabla(name) VALUES ('$elnombre')";

mysqli_query($link,$queryInsert);

$result = mysqli_query($link,$query);

while ($row = mysqli_fetch_assoc($result))
{
    echo $row['name'], PHP_EOL;
}
mysqli_close($link);

} else {
    echo "no parameters";
}

?>
