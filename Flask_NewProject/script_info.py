
def run(projectName):
    run = """from {} import app

if __name__ == "__main__":
app.run()""".format(projectName)

    return run
