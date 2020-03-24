Java.perform(function () {
    var tt1 = Java.use("com.ss.sys.ces.gg.tt$1");
    tt1.a.implementation = function (url, map) {
        console.log(url);
        console.log(map);
        var ret = this.a(url, map);
        console.log(ret);
        return ret;
    }
});

rpc.exports = {
    "sign": function (url, headers) {
        var data = {};
        Java.perform(function () {
            var tt1 = Java.use("com.ss.sys.ces.gg.tt$1").$new();
            const headersMap = Java.use("java.util.TreeMap").$new();
            for (var key in headers) {
                if (headers.hasOwnProperty(key)) {
                    var header = Java.use("java.util.ArrayList").$new();
                    header.add(String(headers[key]));
                    headersMap.put(key, header);
                }
            }
            var result = tt1.a(url, headersMap);
            // console.log(result);
            data["X-Gorgon"] = result.get("X-Gorgon").toString();
            data["X-Khronos"] = result.get("X-Khronos").toString();
        });
        return data;
    }
};
