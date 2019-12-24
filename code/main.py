from EntityExtraction import merge
from RelationExtraction import merge_relation
from Write2Neo import writeneo4j

if __name__=="__main__":
    test_context = "The price of Sony is higer than Panasonic"
    # test_context = "Sony's slide volume is better than Panasonic's"
    # test_context = "Sony is better than apple"
    # test_context = "Sony's mdr-6 better than nwe395."
    # test_context = "Sony mdrv6 is worse than nwe395."
    # test_context = "Sony is invented by nwe395"
    # test_context = "Sony invented nwe395."
    # test_context = "Sony or Panasonic is better than Sennheiser."
    # test_context = "Sony's earphone is better than apple"
    # test_context = "Sony mdrv6 is better than Sennheiser."
    # test_context = "the clarity and definition was also better on the sony, but again, i would expect it to be for the price."

    test_sentence = test_context.lower()
    entities = merge(test_context)
    for i in range(len(entities)):
        if i+1 < len(entities):
            print([entities[i][0],
                  merge_relation(test_context[entities[i][1] + len(entities[i][0]): entities[i+1][1]]),
                  entities[i+1][0]])

            try:
                writeneo4j(entities[i][0],
                           entities[i + 1][0],
                           str(merge_relation(test_context[entities[i][1] + len(entities[i][0]): entities[i+1][1]])))

            except Exception as e:
                print("WARNING: The local neo4j database has something wrong", e)


