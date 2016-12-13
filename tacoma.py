# Numerical Analysis 1
# Group Assignment #3 - The Tacoma Narrows Bridge
#
# Authors:
#   David Andrews
#   Giovanni Arias
#   Cameron Bramwell
#   William Rooney
#   Nikolai Sharp
#   Kaiqi Zhang

import numpy as np
import matplotlib.pyplot as plt
import math

class tacoma:
	def __init__(self, inter, ic, n, p):
		self.debug = True

		self.len = 6
		self.a = 0.2
		self.w = 80
		self.omega = 2*np.pi*38/60
		self.inter = inter
		self.ic = ic
		self.n = n
		self.p = p
		self.h = (inter[1] - inter[0]) / self.n

		yInit = []
		self.y = []
		for i in ic:
			yInit.append(i)
		if self.debug:
			print "yInit:",yInit
		self.y.append(yInit)

		# TODO: Initialize self.y dimensions
		# TODO: Initialize self.t & dimensions with 'inter'

	def setLen(self, len):
		self.len = len

	def setA(self, a):
		self.a = a

	def setW(self, w):
		self.w = w

	def setOmega(self, omega):
		self.omega = omega

	def run(self):
		"""
		Matlab Code:

		t(1)=inter(1);
		set(gca,'XLim',[-8 8],'YLim',[-8 8], ...
		   'XTick',[-8 0 8],'YTick',[-8 0 8], ...
		   'Drawmode','fast','Visible','on','NextPlot','add');
		cla;                                 % clear screen
		axis square                          % make aspect ratio 1 - 1
		road=line('color','b','LineStyle','-','LineWidth',5,...
		    'erase','xor','xdata',[],'ydata',[]);
		lcable=line('color','r','LineStyle','-','LineWidth',1,...
		    'erase','xor','xdata',[],'ydata',[]);
		rcable=line('color','r','LineStyle','-','LineWidth',1,...
		    'erase','xor','xdata',[],'ydata',[]);
		for k=1:n
		  for i=1:p
		    t(i+1) = t(i)+h;
		    y(i+1,:) = trapstep(t(i),y(i,:),h);
		  end
		  y(1,:) = y(p+1,:);t(1)=t(p+1);
		  z1(k)=y(1,1);z3(k)=y(1,3);
		  c=len*cos(y(1,3));s=len*sin(y(1,3));
		  set(road,'xdata',[-c c],'ydata',[-s-y(1,1) s-y(1,1)])
		  set(lcable,'xdata',[-c -c],'ydata',[-s-y(1,1) 8])
		  set(rcable,'xdata',[c c],'ydata',[s-y(1,1) 8])
		  drawnow; pause(h)

		"""

		# TODO: Set up plot
		# t(1)=inter(1);
		#set(gca,'XLim',[-8 8],'YLim',[-8 8], ...
		#	'XTick',[-8 0 8],'YTick',[-8 0 8], ...
		#	'Drawmode','fast','Visible','on','NextPlot','add');
		#cla;                                 % clear screen
		#axis square                          % make aspect ratio 1 - 1
		#road=line('color','b','LineStyle','-','LineWidth',5,...
		#	'erase','xor','xdata',[],'ydata',[]);
		#lcable=line('color','r','LineStyle','-','LineWidth',1,...
		#	'erase','xor','xdata',[],'ydata',[]);
		#rcable=line('color','r','LineStyle','-','LineWidth',1,...
		#	'erase','xor','xdata',[],'ydata',[]);

		z1 = []
		z3 = []
		for k in range(0, self.n-1):
			for i in range(0, self.p):
				self.t[i+1] = self.t[i]+h;
				for j in range(self.y[i]):
					self.y[i+1][j] = self.trapstep(self.t[i],self.y[i][j], self.h) # might be incorrect -> maybe self.y[i] (entire row) is passed?
			for i in range(self.y[i]):
				self.y[0][i] = self.y[self.p][i]
				self.t[0] = self.t[self.p]
			z1.append(self.y[0][0])
			z3.append(self.y[0][2])
			c = self.len*math.cos(self.y[0][2])
			s = self.len*math.sin(self.y[0][2])
			# TODO: Draw lines
			#set(road,'xdata',[-c c],'ydata',[-s-y(1,1) s-y(1,1)])
			#set(lcable,'xdata',[-c -c],'ydata',[-s-y(1,1) 8])
			#set(rcable,'xdata',[c c],'ydata',[s-y(1,1) 8])
			#drawnow; pause(h)

	def trapstep(self, t, x, h):
		""" One step of the Trapezoid Method """
		# More work needed here
		z1 = self.ydot(t, x);
		g = x+h*z1
		z2 = self.ydot(t+h, g);
		return x+h*(z1 +z2)/2

	def ydot(self, t, y):
		# More work needed here
		a1 = math.exp(self.a*(y[0]-self.len*math.sin(y[2])))
		a2 = math.exp(self.a*(y[0]+self.len*math.sin(y[2])))
		self.ydotVals[]
		self.ydotVals.append(y[1])
		self.ydotVals.append(-0.01*y[1] - 0.4*(a1+a2-2) / self.a + 0.2*self.w*math.sin(self.omega*t))
		self.ydotVals.append(y[3])
		self.ydotVals.append(-0.01*y[3] + 1.2*math.cos(y[2])*(a1-a2)/(self.len*self.a))
