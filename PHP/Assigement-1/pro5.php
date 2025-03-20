<html>
    <body>
        <form action="" method="POST">
            NUM 1<input type="number" id="first" name="first"><br>
            NUM 2<input type="number" id="sec" name ="sec"><br>
            NUM 3<input type="number" id="th" name="th"><br>
            <button type="submit" id="but" name="but">SUBMIT</button>
        </form>
    </body>
</html>
<?php
    if (isset($_POST['but'])){
        $num1=$_POST['first'];
        $num2=$_POST['sec'];
        $num3=$_POST['th'];
        $max=max($num1,$num2,$num3);
        $min=min($num1,$num2,$num3);
        echo "max :$max";
        echo "<br>";
        echo "min :$min";
    } 
?>