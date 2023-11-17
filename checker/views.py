from django.shortcuts import render
# from django.views.generic import View
from .prime import PrimeNumberGenerator
# Create your views here.


# myapp/views.py

class PrimeNumberView:
    @staticmethod
    def index(request):
        return render(request, 'index.html')

    @staticmethod
    def generate_primes_view(request):
        try:
            lower_limit = int(request.GET.get('lower_limit', 1))
            upper_limit = int(request.GET.get('upper_limit', 100))

            if lower_limit < 1 or upper_limit < lower_limit:
                raise ValueError("Invalid input. Please ensure the lower limit is at least 1, and the upper limit is greater than or equal to the lower limit.")

            primes = PrimeNumberGenerator.generate_primes(lower_limit, upper_limit)
            return render(request, 'primes.html', {'primes': primes, 'lower_limit': lower_limit, 'upper_limit': upper_limit})

        except ValueError as ve:
            return render(request, 'errors.html', {'error_message': f"Error: {ve}"})
        except Exception as e:
            return render(request, 'errors.html', {'error_message': f"An unexpected error occurred: {e}"})


