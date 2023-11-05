using Newtonsoft.Json;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;

namespace FindIt
{
    public class FindIt
    {
        public class Point
        {
            public double x { get; set; }
            public double y { get; set; }
        }

        public static object GetTrees(string url, string image_path)
        {
            var client = new HttpClient();
            var request = new HttpRequestMessage(HttpMethod.Post, url);
            var content = new MultipartFormDataContent();
            content.Add(new StreamContent(File.OpenRead(image_path)), "file", image_path);
            request.Content = content;
            var response = client.SendAsync(request).Result;
            response.EnsureSuccessStatusCode();
            string body = response.Content.ReadAsStringAsync().Result;

            // Deserialize the JSON to a list of Point objects
            var points = JsonConvert.DeserializeObject<List<Point>>(body);

            // Convert to a list of lists
            var listOfLists = new List<List<double>>();
            foreach (var point in points)
            {
                listOfLists.Add(new List<double> { point.x, point.y });
            }

            return listOfLists;
        }
    }
}