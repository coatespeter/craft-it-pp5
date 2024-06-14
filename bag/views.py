from django.shortcuts import render, redirect, reverse, HttpResponse
import json

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})

    if size:
        if item_id in bag:
            if 'items_by_size' not in bag[item_id]:
                bag[item_id]['items_by_size'] = {}
            if quantity > 0:
                bag[item_id]['items_by_size'][size] = quantity
            else:
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id, None)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        size = request.POST.get('product_size', None)
        bag = request.session.get('bag', {})

        print(f"Removing item_id: {item_id} with size: {size}")
        print(f"Bag before removal: {json.dumps(bag, indent=2)}")

        if item_id in bag:
            if size and 'items_by_size' in bag[item_id] and size in bag[item_id]['items_by_size']:
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    del bag[item_id]
            elif not size:
                del bag[item_id]

        print(f"Bag after removal: {json.dumps(bag, indent=2)}")

    except KeyError as e:
        print(f"KeyError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    request.session['bag'] = bag
    return HttpResponse(status=200)
