from flask import Flask, request, render_template_string
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

HTML = """
<h2>Trade Remedies – Import Analysis Tool</h2>
<form method="POST" enctype="multipart/form-data">
  <p>Upload CSV file:</p>
  <input type="file" name="file">
  <input type="submit" value="Analyze">
</form>

{% if table %}
<h3>Data Preview</h3>
{{ table|safe }}

<h3>Import Trend Chart</h3>
<img src="data:image/png;base64,{{ chart }}">
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files['file']
        df = pd.read_csv(file)

        # Generate chart
        plt.figure()
        df.iloc[:,1].plot()
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        chart = base64.b64encode(buf.getvalue()).decode()

        return render_template_string(HTML, table=df.head().to_html(), chart=chart)

    return render_template_string(HTML, table=None, chart=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
