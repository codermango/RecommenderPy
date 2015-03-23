<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="css/base.css">
        <script type="text/javascript" src="js/base.js"></script>
    </head>
    <body onload="startLoad()">
        <div id="main">
            <div id="liked-movies">
                <ul id="liked-movies-list" class="drop-buckets">
                    <?php
                        $fileArr = array();
                        $file = fopen("../recommender/mark_liked_movie_id.txt", "r") or die("no such file!!");
                        while (!feof($file)) {
                            $id = fgets($file);
                            $fileArr[] = $id;
                        }
                        fclose($file);

                        foreach ($fileArr as $id) {
                            echo "<li>$id</li>";
                        }
                    ?>

                </ul>
            </div>
            <div id="recommended-movies">
                <ul id="recommended-movies-list">
                    <?php
                        //system("python ../recommender/recommender.py");
                        $result = exec("python ../demo/test.py");
                        echo "==". $result. "===";
                    ?>
                </ul>
            </div>
        </div>
    </body>
</html>