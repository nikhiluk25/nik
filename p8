<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diffie-Hellman Key Exchange</title>
</head>
<body>
    <h2>Diffie-Hellman Key Exchange</h2>
    <div>
        <label for="p">Prime Number (p):</label>
        <input type="text" id="p">
    </div>
    <div>
        <label for="g">Primitive Root (g):</label>
        <input type="text" id="g">
    </div>
    <div>
        <label for="privateA">Private Key A (a):</label>
        <input type="text" id="privateA">
    </div>
    <div>
        <label for="privateB">Private Key B (b):</label>
        <input type="text" id="privateB">
    </div>
    <div>
        <button onclick="calculatePublicKey()">Calculate Public Keys</button>
    </div>
    <div>
        <label for="publicA">Public Key A (A):</label>
        <span id="publicA"></span>
    </div>
    <div>
        <label for="publicB">Public Key B (B):</label>
        <span id="publicB"></span>
    </div>
    <div>
        <button onclick="calculateSharedSecret()">Calculate Shared Secret</button>
    </div>
    <div>
        <label for="sharedSecret">Shared Secret:</label>
        <span id="sharedSecret"></span>
    </div>

    <script>
        function calculatePublicKey() {
            var p = parseInt(document.getElementById("p").value);
            var g = parseInt(document.getElementById("g").value);
            var privateA = parseInt(document.getElementById("privateA").value);
            var privateB = parseInt(document.getElementById("privateB").value);

            var publicA = Math.pow(g, privateA) % p;
            var publicB = Math.pow(g, privateB) % p;

            document.getElementById("publicA").innerText = publicA;
            document.getElementById("publicB").innerText = publicB;
        }

        function calculateSharedSecret() {
            var p = parseInt(document.getElementById("p").value);
            var privateA = parseInt(document.getElementById("privateA").value);
            var publicB = parseInt(document.getElementById("publicB").innerText);

            var sharedSecret = Math.pow(publicB, privateA) % p;

            document.getElementById("sharedSecret").innerText = sharedSecret;
        }
    </script>
</body>
</html>
