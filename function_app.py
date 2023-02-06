import logging
import azure.functions as func

logging.basicConfig(level=logging.ERROR)

app = func.FunctionApp()

@app.function_name(name="EventHubTrigger1")
@app.cosmos_db_output(arg_name="doc", database_name="iotdb", collection_name="sensorcopy1", connection_string_setting="connection_string_setting", create_if_not_exists=True, partition_key="/deviceid")
@app.event_hub_message_trigger(arg_name="myhub", event_hub_name="",connection="connectionString")
def test_function(myhub: func.EventHubEvent,  doc: func.Out[func.Document]):
    logging.info('Python EventHub trigger processed an event: %s', myhub.get_body().decode('utf-8'))
    doc.set(func.Document.from_json(myhub.get_body().decode('utf-8')))
