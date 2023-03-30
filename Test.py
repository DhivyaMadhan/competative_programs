import json
var = ['When you face a parenting challenge—disruptive behavior, big emotions, or your own frustration—a short and simple go-to phrase can be your ticket to quickly settling problems in the moment.', '“By using simple and concise phrases, we can avoid getting into lengthy arguments or debates with our children, which can escalate emotions and lead to negative outcomes,” said psychologist and family interventionist Vanessa Kahlon.', ' “One-liners can help us remain calm and composed in stressful situations, as they provide a clear and consistent message to our children.', 'We’ve all had those parenting moments where our child is emotional or just plain irritating, and we say something out of anger that makes everyone feel worse.', ' Once you have a bank of one-liners to tap into, you can create a pause in the drama, allowing everyone to calm down.']
for index, value in enumerate(var):
    # print(int(index)+1, len(value.split()), value)
    dict_value = {"line number": int(index)+1, "number of words":len(value.split()), "Text": value}
    print("dict_value", dict_value)
    print("json", json.dumps(dict_value))





# var1 = "When you face a parenting challenge—disruptive behavior, big emotions, or your own frustration—a short and simple go-to phrase can be your ticket to quickly settling problems in the moment."
# print(var1.split())
# print(len(var1.split()))

