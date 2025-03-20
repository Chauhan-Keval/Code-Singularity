<html>
  <head>
    <style>
      body {
        margin: 0;
        padding: 0;
        font-family: Arial, Helvetica, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      form {
        background-color: aqua;
      }
      input[type=""] {
        padding: 10px;
        margin: 10px;
        border-radius: 5px;
        border: none;
        color: white;
        background-color: blue;
      }
      input[type=""]:hover {
        background-color: black;
      }
    </style>
  </head>
  <body>
    <div>
      <form action="pro7.php" method="GET">
        <table>
          <tr>
            <td><label for="">Enter no 1:</label></td>
            <td><input type="number" name="i1" /></td>
          </tr>
          <tr>
            <td><label for="">Enter no 2:</label></td>
            <td><input type="number" name="i2" /></td>
          </tr>
          <tr>
            <div id="button">
              <td colspan="2">
                <input type="submit" value="Add" name="b1" />
                <input type="submit" value="Sub" name="b2" />
                <input type="submit" value="Mul" name="b3" />
                <input type="submit" value="Div" name="b4" />
              </td>
            </div>
          </tr>
        </table>
      </form>
    </div>
  </body>
</html>
