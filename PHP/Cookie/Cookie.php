<?php
setcookie("Category", "Furniture", time()+86400, "/"," ", 0);
if(isset($_COOKIE["Category"])) {
    echo "Cookie is set".$_COOKIE["Category"];
} else {
    echo "Cookie is not set";
}
?>