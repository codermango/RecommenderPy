<!DOCTYPE HTML>
<html>
    <head>
        <style type="text/css">
            #div1, #div2 { 
                width:500px; 
                height: 100px; 
                margin:10px;
                padding:10px;
                border:1px solid #aaaaaa;
            }

            #div2 {
                width:100px; 
                height:35px; 
                margin:10px;
                padding:10px;
                border:1px solid #aaaaaa;
            }
        </style>
        <script type="text/javascript">
            function myClick() {
                alert("aaa");
            }
        </script>
    </head>
    <body>
        <div id="div1" onclick="myClick()">
            <div id="div2">
                <?php
                    echo "string";
                    system("python ../recommender/recommender.py");
                    system("dir");
                ?>
            </div>
        </div>
        
    </body>
</html>
