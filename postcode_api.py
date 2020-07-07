from pc_lib.single_pc import SinglePC

class PostcodesDataService:

    def single_postcode_data(self, postcode):
        return SinglePC(postcode)


postcodes_call = PostcodesDataService().single_postcode_data('se120nb')
print(postcodes_call.response().postcode)