from itemadapter import ItemAdapter

class ArxivspiderPipeline:
    def process_item(self, item, spider):
        
        return(dict(
            category=item['category_name'],
            latest=dict(zip(item['latest_name'], item['latest_link'])),
            subcategory=dict(zip(item['subcategory_name'], item['subcategory_link']))
                ))
