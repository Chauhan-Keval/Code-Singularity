<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="second.php" method="post">
        <table>
            <tr>
                <td>Name :</td>
                <td><input type="text" name="i1"></td>
            </tr>
            <tr>
                <td>City :</td>
                <td>
                    <select>
                        <option name="rajkot" id="s1">Rajkot</option>
                        <option name="surat" id="s2">Surat</option>
                        <option name="ahmedabad" id="s3">Ahmedabad</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td>Gender :</td>
                <td>
                    <input type="radio" name="r1"/>M
                    <input type="radio" name="r1"/>F
                </td>
            </tr>
            <tr>
                <td>Hobby :</td>
                <td>
                    <input type="checkbox" name="c1"/>Music 
                    <input type="checkbox" name="c2"/>Dance
                    <input type="checkbox" name="c3"/>Reading
                </td>
            </tr>
            <tr>
                <td>Image</td>
                <td>
                    <input type="file" name="f1" value="Browse"/>
                </td>
            </tr>
            <tr>
                <td style="text-align: center;" colspan="2">
                    <input type="submit" value="Submit"/>
                </td>
            </tr>
        </table>
    </form>
</body>
</html>